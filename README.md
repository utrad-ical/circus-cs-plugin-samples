# CIRCUS CS Plug-in Samples

This repository contains minimalistic samples to to build CIRCUS CS plug-ins.

The only required file is `plugin.json`, which must be placed at the
root directory `/` of the Docker image.
This JSON file must contain the following data:

- `pluginName`: The human-readable name for this plug-in.
- `version`: The semver-compatible version.
- `description`: The descriptoin of this plug-in.
- `icon`: (optional) The default icon.
- `displayStrategy`: (optional) Controls how the results will be displayed
  and how feedback will be collected.

## Build and Install a Plug-in

```bash
$ cd javascript/dummy-detection
$ docker build -t circus/dummy-detection:1.0.0 .

$ cd /path/to/circus-api
$ node circus register-cad-plugin <full-image-id>
```

The full image ID (sha256) can be obtained by:

```bash
$ docker image ls --no-trunc
```
