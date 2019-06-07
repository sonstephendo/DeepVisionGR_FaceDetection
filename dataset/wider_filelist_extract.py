import argparse
import sys


def getFilesName(targetFile, outputFile, limit):
    data = []
    with open(targetFile) as f:
        line = f.readline().strip()
        while line:
            if limit and len(data) == int(limit):
                break
            imFilename = line
            folder, basename = imFilename.split("/")
            nbBndboxes = f.readline().strip()
            if int(nbBndboxes) == 0:
                f.readline()
            else:
                i = 0
                while i < int(nbBndboxes):
                    i = i + 1
                    f.readline()
            print("{}".format(basename))
            data.append(basename.replace(".jpg", ""))
            line = f.readline().strip()
    with open(outputFile, "w") as out_file:
        out_file.write("\n".join(data))


def parse_args():
    parser = argparse.ArgumentParser(
        description="Get WIDER filenames from WIDER annotations"
    )
    parser.add_argument(
        "-ap",
        dest="annotations_path",
        required=True,
        help='the annotations file path. ie: "-ap wider_face_train_bbx_gt.txt".',
    )
    parser.add_argument(
        "-o",
        dest="output",
        required=True,
        help='the target output files will be saved. ie: "-o wider_face_train_filelist.txt"',
    )
    parser.add_argument(
        "-l", dest="limit", help="The exactly size of image list. ie: 100"
    )
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = parse_args()
    getFilesName(args.annotations_path, args.output, args.limit)
    # python3 wider_filelist_extract.py -ap wider_face_train_bbx_gt.txt -o wider_face_train_filelist.txt
    # python3 wider_filelist_extract.py -ap wider_face_val_bbx_gt.txt -o wider_face_val_filelist.txt
