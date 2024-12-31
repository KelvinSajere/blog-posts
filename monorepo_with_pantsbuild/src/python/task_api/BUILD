python_sources()


pex_binary(
    name="task_api_binary",
    entry_point="main.py",
    complete_platforms=["src/python/complete_platforms:python_3.10_slim_amd"],
)

docker_image(
    name="task_api_image",
    image_tags=["1.22"],
    repository="social-media-443307/social-media/{directory}",
    registries=["us-west3-docker.pkg.dev"],
    build_platform=["linux/amd64"],
)


adhoc_tool(
    name="extract_version",
    runnable="src/python/deployments:extract_version",
    args=[
        "--json-path",
        "{chroot}/src.python.task_api/task_api_image.docker-info.json",
        "--yaml-path",
        "{chroot}/src/python/task_api/deploy.yaml",
    ],
    output_directories=["deployments"],
    execution_dependencies=[":task_api_image", ":deployment_spec"],
    log_output=True,
    root_output_directory=".",
)

resource(name="deployment_spec", source="deploy.yaml")

run_shell_command(
    name="deploy",
    command="gcloud run services replace {chroot}/deployments/deploy.yaml",
    execution_dependencies=[":extract_version"],
    tags=["deployment"],
)
