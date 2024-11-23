system_binary(
    name="touch",
    binary_name="touch",
    #fingerprint=r"1\.([2-9][0-9]|[1-9][0-9][0-9])\..*",
    fingerprint_args=["--version"],
    #fingerprint_dependencies=[":node"],
)

adhoc_tool(
    name="build_resources",
    runnable=":touch",
    #runnable_dependencies=[":touch"],
    args=["touch", "generated.txt"],
    output_directories=["./"],
    timeout=300,
)

# because of a bug we have to relocate the resources
# see: https://github.com/pantsbuild/pants/issues/21444
relocated_files(
    name="relocated_resources",
    src="src/python/example",
    dest="example",
    files_targets=[":build_resources"],
)

experimental_wrap_as_resources(
    name="wrapped_resources",
    inputs=[":relocated_resources"],
)

python_sources(
    name="src",
    dependencies=[
        ":wrapped_resources",
    ],
)

pex_binary(
    name="loose",
    dependencies=[
        ":src"
    ],
    layout="loose",
    entry_point="main.py",

)

pex_binary(
    name="zipapp",
    dependencies=[
        ":src"
    ],
    entry_point="main.py",
)
