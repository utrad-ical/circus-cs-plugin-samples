# CIRCUS CS Plug-in Samples

## Build and Install a Plug-in

```bash
cd javascript/dummy-detection
docker build -t circus/dummy-detection:1.0.0 .

cd /path/to/circus-api
node circus register-cad-plugin <full-image-id>
```

The full image ID (sha256) can be obtained by:

```bash
docker image ls --no-trunc
```
