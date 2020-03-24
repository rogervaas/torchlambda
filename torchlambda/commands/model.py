import pathlib
import zipfile

from .. import utils


def run(args):
    destination = pathlib.Path(args.destination).absolute()
    with utils.general.message("packing Torchscript model to {}.".format(destination)):
        with zipfile.ZipFile(
            destination,
            "w",
            compression=getattr(zipfile, "ZIP_{}".format(args.compression)),
            compresslevel=utils.model.compression_level(args.compression, args.level),
        ) as file:
            utils.model.validate(args)
            file.write(
                pathlib.Path(args.source),
                utils.model.path(args) if args.directory is not None else args.source,
            )
