
import json
import numpy as np
from scipy import ndimage
from skimage import io, filters


def _extract_largest_area(data, dimension=3):

    structure = np.ones([3,3]) if dimension == 2 else np.ones([3,3,3]) 
    
    labeled, num_labels = ndimage.label(data, structure)
    largest_idx = 0

    if num_labels > 1:
        hist = ndimage.histogram(labeled, 1, num_labels, num_labels)
        largest_idx = np.argmax(hist)
    
    return (labeled == largest_idx + 1).astype(np.uint8)   


def _body_trunk_extraction(volume, threshold):
    
    body_trunk = np.zeros(volume.shape, dtype=np.uint8)

    for n in range(0, volume.shape[0]):
        
        # thresholding
        mask_img = (volume[n,:,:] >= threshold) + 0
        
        # Extract the largest area
        mask_img = _extract_largest_area(mask_img, 2)
        mask_img = ndimage.morphology.binary_fill_holes(mask_img)

        body_trunk[n,:,:] = mask_img

    # Final extraction
    body_trunk = _extract_largest_area(body_trunk, 3)
   
    return body_trunk


def do_detection(in_path, out_path):

    in_volume_file_name = "%s/0.mhd" % (in_path)
    result_file_name = "%s/results.json" % (out_path)

    volume = io.imread(in_volume_file_name, plugin='simpleitk')    

    # thresholding by Otsu's method
    threshold = filters.threshold_otsu(volume)

    body_trunk = _body_trunk_extraction(volume, threshold)

    body_trunk_pos = np.where(body_trunk)
    crop_origin = [int(np.min(body_trunk_pos[2])),
                   int(np.min(body_trunk_pos[1])),
                   int(np.min(body_trunk_pos[0]))]
    crop_size = [int(np.max(body_trunk_pos[2]) - np.min(body_trunk_pos[2])),
                 int(np.max(body_trunk_pos[1]) - np.min(body_trunk_pos[1])),
                 int(np.max(body_trunk_pos[0]) - np.min(body_trunk_pos[0]))]

    results = {}
    results["displayOptions"] = {"volumeId": 0,
                                 "crop": { "origin": crop_origin, "size": crop_size}}

    lesion_candidates = []
    rank = 1
    confidence = 1.0

    while rank <= 3:

        cand_pos_x = int(np.random.randint(crop_origin[0], crop_origin[0] + crop_size[0]))
        cand_pos_y = int(np.random.randint(crop_origin[1], crop_origin[1] + crop_size[1]))
        cand_pos_z = int(np.random.randint(crop_origin[2], crop_origin[2] + crop_size[2]))

        if body_trunk[cand_pos_z, cand_pos_y, cand_pos_x] == 1:
            tmp_candidate = {"rank": rank,
                             "confidence": confidence,
                             "volumeId": 0,
                             "location": [cand_pos_x, cand_pos_y, cand_pos_z]}
            lesion_candidates.append(tmp_candidate)
            rank += 1
            confidence /= 2.0

    results["results"] = {"lesionCandidates": lesion_candidates}

    print(results)

    with open(result_file_name, "w", encoding="utf-8") as fp:
        json.dump(results, fp, indent=4)


if __name__ == '__main__':

    in_path = "/circus/in"
    out_path = "/circus/out"

    do_detection(in_path, out_path)
