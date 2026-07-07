class DBAccessViolation:

    def __init__(self, source_file, database_library):

        self.source_file = source_file
        self.database_library = database_library


class DBAccessAnalyzer:

    DB_LIBRARIES = {

        "mongoose",
        "sequelize",
        "prisma"


    }

    def analyze(self, dependencies ):

        violations = []

        for dependency in dependencies:

          source_layer = self.get_layer(dependency.source_file)

          if source_layer != "controllers":

              continue

          for db_library in self.DB_LIBRARIES:

            if db_library in dependency.target_module:

                violations.append(

                    DBAccessViolation(

                        dependency.source_file,

                        db_library
                    )
                )

        return violations
    

    def get_layer(self,module_name):

        parts = module_name.split(".")

        for part in parts:

            if part in {
                "controllers",
                "services",
                "repositories"
            }:
                return part
        return None
            

        