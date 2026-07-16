def get_layer(
    module_name
):

    parts = module_name.split(".")

    for part in parts:

        if part in {

            "controllers",
            "services",
            "repositories"

        }:

            return part

    return None