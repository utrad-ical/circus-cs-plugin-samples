FROM continuumio/miniconda3:4.9.2

# Add packages
RUN pip install --no-cache-dir\
        numpy\
        scipy\
        scikit-image\
        simpleitk

# Add plugin manifest file.
COPY plugin.json /

# Add main script for this CAD.
COPY src/* /plugin/

# This is the main entry point when this container is invoked.
CMD ["python", "/plugin/random_detection.py"]
