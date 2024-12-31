import argparse
import json
from pathlib import Path

from ruamel.yaml import YAML


def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Consume a JSON file.")
    parser.add_argument("--json-path", required=True, help="Path to the JSON file")
    parser.add_argument("--yaml-path", required=True, help="Path to the JSON file")

    args = parser.parse_args()

    json_path = args.json_path
    yaml_path = args.yaml_path

    image_name = extract_image_name(json_path)

    update_yaml(yaml_path, image_name)



def update_yaml(
    yaml_path: str,
    image_name: str,
):
    yaml = YAML()

    # Read the YAML file
    with open(yaml_path, "r") as file:
        data = yaml.load(file)

    # Replace $name with 'helloworld'
    containers = data["spec"]["template"]["spec"]["containers"]
    for container in containers:
        if container.get("image") == "$name":
            container["image"] = image_name

    target = "deployments/deploy.yaml"

    Path(target).parent.mkdir(exist_ok=True, parents=True)
    with open(target, "w") as file:
        yaml.dump(data, file)

    print(f"Running deployment against {image_name}")


def extract_image_name(json_path: str) -> str:
    with open(json_path, "r") as json_file:
        json_dict = json.load(json_file)
        return json_dict["registries"][0]["tags"][0]["name"]


if __name__ == "__main__":
    main()
