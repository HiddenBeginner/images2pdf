import glob
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Image, PageBreak, Frame, PageTemplate

def get_document(args, rightMargin=2.5*mm, leftMargin = 2.5*mm, topMargin = 2.5*mm, bottomMargin = 2.5*mm):
    save_path = f'{args.title}.pdf'
    doc = SimpleDocTemplate(save_path)
    doc.title = args.title

    doc.rightMargin = rightMargin
    doc.leftMargin = leftMargin
    doc.topMargin = topMargin
    doc.bottomMargin = bottomMargin
    doc.width = A4[0] - (doc.rightMargin + doc.leftMargin)
    doc.height = A4[1] - (doc.topMargin + doc.bottomMargin)

    return doc

def get_maximum_image_size(doc):
    frameT = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height)

    max_width = frameT._getAvailableWidth()
    max_height = frameT._aH

    return max_width, max_height

def get_image(image, max_width, max_height):
    im = ImageReader(image)
    w, h = im.getSize()
    ratio = h / w

    if (w > max_width) or (h > max_height):
        if ratio > 1:
            return Image(image, width=max_height / ratio, height=max_height)
        else:
            return Image(image, width=max_width, height=max_weight * ratio)
    else:
        return Image(image)

def run(args):
    # Initialize pdf file
    doc = get_document(args)

    # Calculate the availble maximum image size
    max_width, max_height = get_maximum_image_size(doc)

    # Insert image to the pdf file
    images = glob.glob(f'{args.images_path}/*')
    parts = []
    for image in images:
        parts.append(get_image(image, max_width, max_height))
        parts.append(PageBreak())

    # Save the pdf file
    doc.build(parts)

def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--images_path", type=str, default="./images")
    parser.add_argument("--title", type=str, default="untitled")
    args = parser.parse_args()

    run(args)

if __name__ == "__main__":
    main()