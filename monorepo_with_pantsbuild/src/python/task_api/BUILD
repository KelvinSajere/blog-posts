python_sources()


pex_binary(
  name="task_api_binary",
  entry_point="main.py",
  complete_platforms = ["src/python/complete_platforms:python_3.10_slim"]
)

docker_image(
    name="task_api_image",
    image_tags = ["1.0"],
    repository = "social-media-443307/social-media/{directory}",
    registries=["us-west3-docker.pkg.dev"]
)
