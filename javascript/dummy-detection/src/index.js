/**
 * CIRCUS CS Plugin Sample - Dummy Lesion Detection
 */

const path = require('path');
const fs = require('fs').promises;

const inDir = '/circus/in';
const outDir = '/circus/out';
const outFile = path.join(outDir, 'results.json');

const result = {
  metadata: {
    displayOptions: [
      {
        volumeId: 0,
        window: { level: -600, width: 1500 },
        crop: { origin: [76, 139, 26], size: [331, 215, 215] }
      }
    ]
  },
  results: {
    lesionCandidates: [
      {
        rank: 1,
        confidence: 0.876,
        volumeId: 0,
        location: [200, 258, 58],
        volumeSize: 50.4
      },
      {
        rank: 2,
        confidence: 0.765,
        volumeId: 0,
        location: [250, 258, 58],
        volumeSize: 31.4
      }
    ]
  }
};

const main = async () => {
  await fs.mkdir(outDir, { recursive: true });
  await fs.writeFile(outFile, JSON.stringify(result), 'utf8');
};

main();
