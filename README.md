# music-presence/protocols

Specifications for open protocols used by Music Presence.

The `src` directory contains the following source files:

- `.proto` files contain definitions for all messages used in protocols
- `.spec.md` files contain detailed descriptions of protocols
- `.guide.md` files contain a comprehensive guide
  on how to integrate specific protocols
  into your application or application plugin,
  such that it can integrate with Music Presence

The `dist` directory contains JSON schema files
generated from `.proto` files in the `src` directory.
The `examples` directory contains examples of valid JSON protocol messages.

To get started, read one of the guides in the `src` directory.

---

## Requirements

- `go` installed and on PATH
- `protoc` installed and on PATH
- `python3` installed and on PATH

## Setup

```
make setup
```

- Downloads all submodules
- Builds all protoc plugins and outputs them in `bin`
- Creates a virtual Python environment in `.venv`
  and installs all dependencies
- Builds protobuf messages for Python

## Build JSON schemas for protocol messages

Make sure `invoke` is installed.

To generate the schema for a single message:

```
inv gen media-channel Hello
```

To generate schemas for all messages in a proto file:

```
inv gen media-channel
```

To generate schemas for all protobuf files:

```
inv gen
```

Make sure to run `make rebuild-py` before `inv gen`
whenever a proto file is changed
or run the convenience make target `make gen`.

Also import all proto files in `tasks.py`
and adapt the global `proto_message_names` dictionary,
whenever a new protocol is added to the `src` directory.
