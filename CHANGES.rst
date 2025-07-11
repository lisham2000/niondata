Changelog (niondata)
====================

15.9.0 (2025-06-25)
-------------------
- Add rectangle mask generation functions.
- Change behavior to use center of pixel to determine if a pixel is within a mask.

15.8.2 (2025-05-27)
-------------------
- Maintenance release to fix a build issue.

15.8.1 (2025-04-23)
-------------------
- Ensure element data always returns actual ndarray.

15.8.0 (2025-01-06)
-------------------
- Add support for 5d (1/2/2) data in data and metadata objects.

15.7.0 (2024-10-27)
-------------------
- Make Calibration hashable.
- Require Numpy 2. Add Python 3.13 support. Drop Python 3.9, 3.10 support.

15.6.3 (2024-06-12)
-------------------
- Restore RPC (remote procedure calls) support to DataAndMetadata.

15.6.2 (2024-01-02)
-------------------
- Add power function (xdata.power).
- Add radial profile function (xdata.radial_profile).
- Improve handing of invalid inverse coordinates (1/0).
- Add support for computing the phase of a complex array (thanks Luc J Bourhis).
- Improve performance (eliminate some unnecessary metadata dict copying)

15.6.1 (2023-10-23)
-------------------
- Minor update for typing compatibility.

15.6.0 (2023-08-17)
-------------------
- Reapply DataMetadata read-only accessors change.
- Make read-only accessors to all DataMetadata properties instead of having them be read/write.

0.15.5 (2023-06-21)
-------------------
- Revert breaking change: DataMetadata read-only accessors.

0.15.4 (2023-06-19)
-------------------
- Introduce rebin_factor xdata function.
- Carry through intensity calibration during FFT/IFFT.
- Add copy magic method to data metadata.
- Make read-only accessors to all DataMetadata properties instead of having them be read/write.
- Require Python 3.9 or higher.

0.15.3 (2022-10-03)
-------------------
- Add is_valid method to calibrations and use when converting to strings.

0.15.2 (2022-09-13)
-------------------
- Add low level functions for general multi-dimensional processing.

0.15.1 (2022-07-25)
-------------------
- Use scipy.fft for FFT's for better/consistent performance.

0.15.0 (2022-02-28)
-------------------
- Add axis_coordinates function to generate coordinate values from calibrated xdata.
- Simplify data and metadata by eliminating unloading capability (no effect on public API).

0.14.3 (2022-02-18)
-------------------
- Fix issue where timezone/timezone_offset could get set to invalid values.
- Improve Gaussian blur to handle RGB.

0.14.2 (2022-01-03)
-------------------
- Improve compatibility with HDF5 backed data (use numpy.copy instead of d.copy).

0.14.1 (2021-12-13)
-------------------
- Enable support for Python 3.10.
- Fix issue for cross correlation using only first image.
- Fix regression with template register using rounded position.
- Extend sequence trim/integrate to work on sequences of collections.
- Fix half-pixel offset in register_template.
- Allow a mask in register_template for fine-tuning maximum finding.

0.14.0 (2021-11-10)
-------------------
- Enable strict typing.
- Drop support for Python 3.7.
- Add auto-thresholding functions.

0.13.15 (2021-05-26)
--------------------
- Optimize element data for sequence + collection case.
- Change sub-pixel registration method to parabola fit to improve speed.

0.13.14 (2021-03-12)
--------------------
- Add affine transform function and optional order parameter to warp.
- Allow zero-dimensioned (scalar) data and metadata objects.

0.13.13 (2020-12-08)
--------------------
- Make special case of C(1) D(1) < 16 from element data function optional.

0.13.12 (2020-10-06)
--------------------
- Fixed RGB issues when data backed by h5py array instead of numpy array.
- Changed rescale to take a new parameter 'in_range'.
- Changed rgba/rgb functions to clip data to 0, 255.
- Split display functions into element and scalar functions.

0.13.11 (2020-08-31)
--------------------
- Introduce calibrated coordinates and reference frames (preliminary).
- Improve handling of NaNs in rebin_1d.
- Add xdata function rebin_image.
- Fix issue with bounds when rotating data.
- Fix issues with concatenate and data descriptor.
- Add xdata functions to split/join sequences.
- Add template matching functions to xdata.
- Make pick functions work for sequences of spectrum images.

0.13.10 (2020-02-26)
--------------------
- Change shift/align functions to use spline-1st-order; add Fourier variants as alternative.
- Fix calibration bug in xdata concatenate (and some cases of hstack, vstack).
- Add function to generate elliptical masks.
- Change FFT to put calibration origin at 0.5, 0.5 pixels from center.

0.13.9 (2019-11-27)
-------------------
- Improve handling of squeeze/calibration for sequence measurements.
- Add new navigation properties (combo of is_sequence and collection) to data.
- Support slicing on RGB sequences (for display data).

0.13.8 (2019-10-24)
-------------------
- Added optional registration area bounds to align and register functions.

0.13.7 (2019-02-27)
-------------------
- Added mean function. Add keepdim param to mean/sum. Allow negative indices.

0.13.6 (2018-12-28)
-------------------
- Fix display RGB calculation on integer images.
- Add methods for better control of data ref count.

0.13.5 (2018-12-11)
-------------------
- Add setters for timezone, timezone_offset, and timestamp.

0.13.4 (2018-11-13)
-------------------
- Add measure_relative_translation function to xdata. Utilize in align.
- Generalize align and register sequence to accept any combo of sequence and collection dimensions.
- Provide more descriptive data dimensions string.

0.13.3 (2018-06-15)
-------------------
- Fix squeeze to not remove last datum dimension.
- Add re-dimension function (changes data description, keeps data layout in memory the same).
- Ensure that data_descriptor is a copy, not a reference, when accessed from DataAndMetadata.
- Add calibration and data_descriptor creation methods to xdata_1_0.
- Change crop to always produce the same size crop, even if out of bounds. Fill out of bounds with zero.
- Add crop_rotated to handle crop with rotation (slower).

0.13.2 (2018-05-23)
-------------------
- Automatically promote ndarray and constants (where possible) to xdata in operations.
- Fix FFT-1D scaling and shifting inconsistency.
- Add average_region function (similar to sum_region).

0.13.1 (2018-05-21)
-------------------
- Fix timezone bug.

0.13.0 (2018-05-10)
-------------------
- Initial version online.
