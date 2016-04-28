# standard libraries

# third party libraries
import numpy

# local libraries
from nion.data import DataAndMetadata
from nion.data import Image

def function_rgb_channel(data_and_metadata, channel):
    def calculate_data():
        data = data_and_metadata.data
        if channel < 0 or channel > 3:
            return None
        if not Image.is_data_valid(data):
            return None
        if Image.is_shape_and_dtype_rgb(data.shape, data.dtype):
            if channel == 3:
                return numpy.ones(data.shape, numpy.int)
            return data[..., channel].astype(numpy.int)
        elif Image.is_shape_and_dtype_rgba(data.shape, data.dtype):
            return data[..., channel].astype(numpy.int)
        else:
            return None

    if not data_and_metadata.is_data_rgb_type:
        return None

    return DataAndMetadata.DataAndMetadata(calculate_data, data_and_metadata.data_shape_and_dtype,
                                           data_and_metadata.intensity_calibration,
                                           data_and_metadata.dimensional_calibrations, data_and_metadata.metadata)


def function_rgb_linear_combine(data_and_metadata, red_weight, green_weight, blue_weight):
    def calculate_data():
        data = data_and_metadata.data
        if not Image.is_data_valid(data):
            return None
        if Image.is_shape_and_dtype_rgb(data.shape, data.dtype):
            return numpy.sum(data[..., :] * (blue_weight, green_weight, red_weight), 2)
        elif Image.is_shape_and_dtype_rgba(data.shape, data.dtype):
            return numpy.sum(data[..., :] * (blue_weight, green_weight, red_weight, 0.0), 2)
        else:
            return None

    if not data_and_metadata.is_data_rgb_type:
        return None

    return DataAndMetadata.DataAndMetadata(calculate_data, data_and_metadata.data_shape_and_dtype,
                                           data_and_metadata.intensity_calibration,
                                           data_and_metadata.dimensional_calibrations, data_and_metadata.metadata)


def function_rgb(red_data_and_metadata, green_data_and_metadata, blue_data_and_metadata):
    def calculate_data():
        shape = tuple(red_data_and_metadata.data_shape)
        rgb_image = numpy.empty(shape + (3,), numpy.uint8)
        channels = (blue_data_and_metadata, green_data_and_metadata, red_data_and_metadata)
        for channel_index, channel in enumerate(channels):
            data = channel.data

            if not Image.is_data_valid(data):
                return None

            if tuple(data.shape) != shape:
                return None

            if data.dtype.kind in 'iu':
                rgb_image[..., channel_index] = data
            elif data.dtype.kind in 'f':
                rgb_image[..., channel_index] = numpy.multiply(data, 255)
            else:
                return None
        return rgb_image

    shape = tuple(red_data_and_metadata.data_shape)

    if tuple(green_data_and_metadata.data_shape) != shape or tuple(blue_data_and_metadata.data_shape) != shape:
        return None

    return DataAndMetadata.DataAndMetadata(calculate_data, red_data_and_metadata.data_shape_and_dtype,
                                           red_data_and_metadata.intensity_calibration,
                                           red_data_and_metadata.dimensional_calibrations, red_data_and_metadata.metadata)


def function_rgba(red_data_and_metadata, green_data_and_metadata, blue_data_and_metadata, alpha_data_and_metadata):
    def calculate_data():
        shape = tuple(red_data_and_metadata.data_shape)
        rgba_image = numpy.empty(shape + (4,), numpy.uint8)
        channels = (blue_data_and_metadata, green_data_and_metadata, red_data_and_metadata, alpha_data_and_metadata)
        for channel_index, channel in enumerate(channels):
            data = channel.data

            if not Image.is_data_valid(data):
                return None

            if tuple(data.shape) != shape:
                return None

            if data.dtype.kind in 'iu':
                rgba_image[..., channel_index] = data
            elif data.dtype.kind in 'f':
                rgba_image[..., channel_index] = numpy.multiply(data, 255)
            else:
                return None
        return rgba_image

    shape = tuple(red_data_and_metadata.data_shape)

    if tuple(green_data_and_metadata.data_shape) != shape or tuple(blue_data_and_metadata.data_shape) != shape or tuple(alpha_data_and_metadata.data_shape) != shape:
        return None

    return DataAndMetadata.DataAndMetadata(calculate_data, red_data_and_metadata.data_shape_and_dtype,
                                           red_data_and_metadata.intensity_calibration,
                                           red_data_and_metadata.dimensional_calibrations, red_data_and_metadata.metadata)
