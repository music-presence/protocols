from invoke import task
from invoke.context import Context as C

from typing import Optional
import sys

sys.path.append("./build/py")
from build.py import media_channel_pb2 as media_channel

proto_message_names = {
    "media-channel": media_channel.DESCRIPTOR.message_types_by_name.keys()
}


@task
def gen_proto_message(c: C, proto: str, message: str):
    if proto not in proto_message_names:
        raise ValueError(f"unknown proto: {proto}")
    if message not in proto_message_names[proto]:
        raise ValueError(f"unknown proto message: {proto}.{message}")
    print(f"generating schema for {proto}.{message}")
    c.run(
        " ".join(
            [
                "protoc",
                "--plugin=protoc-gen-jsonschema=./bin/protoc-gen-jsonschema",
                "--jsonschema_out=./dist/schemas",
                f"--jsonschema_opt=entrypoint_message={message}",
                f"--jsonschema_opt=output_file_suffix=.{message}.schema.json",
                "-I ./third_party/protoc-gen-jsonschema",
                "-I ./src",
                f"./src/{proto}.proto",
            ]
        )
    )


@task
def gen_all_messages(c: C, proto: str):
    for message in proto_message_names[proto]:
        gen_proto_message(c, proto, message)


@task
def gen_all_protos(c: C):
    for proto in proto_message_names.keys():
        gen_all_messages(c, proto)


@task
def gen(c: C, proto: Optional[str] = None, message: Optional[str] = None):
    if proto is None:
        gen_all_protos(c)
    elif message is None:
        gen_all_messages(c, proto)
    else:
        gen_proto_message(c, proto, message)
