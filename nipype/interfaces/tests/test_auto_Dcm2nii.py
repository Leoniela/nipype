# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.dcm2nii import Dcm2nii

def test_Dcm2nii_inputs():
    input_map = dict(anonymize=dict(argstr='-a',
    usedefault=True,
    ),
    args=dict(argstr='%s',
    ),
    collapse_folders=dict(argstr='-c',
    usedefault=True,
    ),
    config_file=dict(argstr='-b %s',
    genfile=True,
    ),
    convert_all_pars=dict(argstr='-v',
    usedefault=True,
    ),
    date_in_filename=dict(argstr='-d',
    usedefault=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    events_in_filename=dict(argstr='-e',
    usedefault=True,
    ),
    gzip_output=dict(argstr='-g',
    usedefault=True,
    ),
    id_in_filename=dict(argstr='-i',
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    nii_output=dict(argstr='-n',
    usedefault=True,
    ),
    output_dir=dict(argstr='-o %s',
    genfile=True,
    ),
    protocol_in_filename=dict(argstr='-p',
    usedefault=True,
    ),
    reorient=dict(argstr='-r',
    ),
    reorient_and_crop=dict(argstr='-x',
    usedefault=True,
    ),
    source_dir=dict(argstr='%s',
    mandatory=True,
    position=-1,
    xor=['source_names'],
    ),
    source_in_filename=dict(argstr='-f',
    usedefault=True,
    ),
    source_names=dict(argstr='%s',
    copyfile=False,
    mandatory=True,
    position=-1,
    xor=['source_dir'],
    ),
    spm_analyze=dict(argstr='-s',
    xor=['nii_output'],
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = Dcm2nii.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_Dcm2nii_outputs():
    output_map = dict(bvals=dict(),
    bvecs=dict(),
    converted_files=dict(),
    reoriented_and_cropped_files=dict(),
    reoriented_files=dict(),
    )
    outputs = Dcm2nii.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

