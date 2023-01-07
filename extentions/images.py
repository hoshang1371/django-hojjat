from django.core.files.base import ContentFile
import os.path
from PIL import Image
from io import BytesIO
import base64


def make_thumbnail(dst_image_field, src_image_field, size, name_suffix, sep='_'):
    """
    make thumbnail image and field from source image field

    @example
        thumbnail(self.thumbnail, self.image, (200, 200), 'thumb')
    """
    # create thumbnail image
    image = Image.open(src_image_field)
    image.thumbnail(size, Image.ANTIALIAS)

    # build file name for dst
    dst_path, dst_ext = os.path.splitext(src_image_field.name)
    dst_ext = dst_ext.lower()
    dst_fname = dst_path + sep + name_suffix + dst_ext

    # print(f"dst_fname: {dst_fname}")

    # check extension
    if dst_ext in ['.jpg', '.jpeg']:
        filetype = 'JPEG'
    elif dst_ext == '.gif':
        filetype = 'GIF'
    elif dst_ext == '.png':
        filetype = 'PNG'
    else:
        raise RuntimeError('unrecognized file type of "%s"' % dst_ext)

    # print(f"dst_ext:{dst_ext}")
    # print(f"filetype:{filetype}")

    # Save thumbnail to in-memory file as StringIO
    dst_bytes = BytesIO()
    image.save(dst_bytes, filetype)
    dst_bytes.seek(0)

    # set save=False, otherwise it will run in an infinite loop
    dst_image_field.save(dst_fname, ContentFile(dst_bytes.read()), save=False)
    dst_bytes.close()


def to_internal_value(self,request):
        datadict = request.data.get('image')
        data = datadict['contents']
        
        if 'data:' in data and ';base64,' in data:
            header, data = data.split(';base64,')
            header = header.split('/')
        try:
            decoded_file = base64.b64decode(data)
        except TypeError:
            self.fail('invalid_image')
        # print(decoded_file)

        complete_file_name = "%s.%s" % (datadict['filename'], header[1], )
        return ContentFile(decoded_file, name=complete_file_name)
