import ast
import os

from CODEGUARDIAN.config.config_loader import ConfigLoader

from CODEGUARDIAN.src.parser.ts_parser import (
    parse_typescript
)

from CODEGUARDIAN.src.tree.Walker import walk

from CODEGUARDIAN.utils.ast_cache import ASTCache
class Dependency:

    def __init__(
        self,
        source_file,
        target_module
    ):

        self.source_file = source_file
        self.target_module = target_module


class DependencyAnalyzer:

    def __init__(self):

        self.config = ConfigLoader.load()

        self.supported_extensions = set(
            self.config["supported_extensions"]
        )

    def analyze_python_file(
        self,
        file_path,
        project_root
    ):

        dependencies = []

        relative_path = os.path.relpath(
            file_path,
            project_root
        )

        module_name = (
            relative_path
            .replace(".py", "")
            .replace(os.sep, ".")
        )

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            source = file.read()
        try:
           tree = ASTCache.get_tree(
           file_path,
           source
           )
        except SyntaxError:
            return []

        for node in ast.walk(tree):

            if isinstance(
                node,
                ast.ImportFrom
            ):

                if node.module:

                    dependencies.append(

                        Dependency(
                            module_name,
                            node.module
                        )
                    )

            elif isinstance(
                node,
                ast.Import
            ):

                for imported in node.names:

                    dependencies.append(

                        Dependency(
                            module_name,
                            imported.name
                        )
                    )

        return dependencies

    def analyze_ts_js_file(
        self,
        file_path,
        project_root
    ):

        dependencies = []

        relative_path = os.path.relpath(
            file_path,
            project_root
        )

        module_name = (
            relative_path
            .replace(".ts", "")
            .replace(".js", "")
            .replace(os.sep, ".")
        )

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            source = file.read()
        try:
            tree = ASTCache.get_tree(
             file_path,
             source
            )
        except Exception:
            return []
        
        if tree.root_node.has_error:
            return []

        def visit(node):

            if node.type != "import_statement":

                return

            source_node = node.child_by_field_name(
                "source"
            )

            if not source_node:

                return

            imported_module = (
                source_node.text
                .decode("utf8")
                .replace('"', "")
                .replace("'", "")
            )
            if imported_module.startswith("./"):

                current_directory = ".".join(
                    module_name.split(".")[:-1]
                )


                if current_directory:
                

                  imported_module = (
                    current_directory
                    + "."
                    + imported_module[2:]
                )
                  
                else:
                    imported_module = imported_module[2:]

                imported_module = imported_module.replace(
                    "/",
                    "."
                )


            resolved_modules = self.resolve_barrel_import(
               imported_module,
               module_name,
               project_root
            )

            for resolved_module in resolved_modules:

              dependencies.append(

                Dependency(
                module_name,
                resolved_module
              )
              )   

            

        walk(
            tree.root_node,
            visit
        )

       
        

        return dependencies
    
    

    def resolve_barrel_import(
      self,
      imported_module,
      module_name,
      project_root
      ):


      


      module_path = os.path.join(
        project_root,
        *imported_module.split(".")
        )
      
      file_ts = module_path + ".ts"
      file_js = module_path + ".js"

      index_ts = os.path.join(
        module_path,
        "index.ts"
       )

      index_js = os.path.join(
        module_path,
        "index.js"
       )

      if os.path.exists(index_ts):
        print("module_path:", module_path)
        print("file_ts:", file_ts)
        print("index_ts:", index_ts)
        barrel_file = index_ts

      elif os.path.exists(index_js):
         barrel_file = index_js

      elif (
        imported_module.endswith("index")
         and  os.path.exists(file_ts)
        ):  
           barrel_file = file_ts

      elif (
        imported_module.endswith("index")
        and os.path.exists(file_js)
       ):
         barrel_file = file_js

      else:
        return [imported_module]
      
     


      

      with open(
        barrel_file,
        "r",
        encoding="utf-8"
      ) as file:
        source = file.read()

      try:
          tree = ASTCache.get_tree(
          barrel_file,
          source
        )
          
          
        
      except Exception:
        return [imported_module]

      resolved_modules = []

      def visit(node):
        

      

      

        if node.type != "export_statement":
          return

        source_node = node.child_by_field_name(
        "source"
         )

        if not source_node:
         
          print(node.sexp())
          return
        
        


       

        exported_module = (
          source_node.text
          .decode("utf8")
          .replace('"', "")
          .replace("'", "")
    )

        if exported_module.startswith("./"):

          current_directory = ".".join(
        imported_module.split(".")[:-1]
        )

          if current_directory:
            exported_module = (
            current_directory
            + "."
            + exported_module[2:]
            )
          else:
            exported_module = exported_module[2:]

          exported_module = exported_module.replace(
           "/",
           "."
           )
          
        

        resolved_modules.append(exported_module)

      walk(
       tree.root_node,
        visit
       )
      

      
      


      if resolved_modules:
        return resolved_modules

      return [imported_module]

      

    

    def analyze_project(
        self,
        project_path
    ):

        dependencies = []

       

        ignore_dirs = set(
            self.config[
                "ignored_directories"
            ]
        )

        for root, dirs, files in os.walk(project_path):

            dirs[:] = [

                d for d in dirs

                if d not in ignore_dirs
            ]

            for file in files:

                extension = os.path.splitext(
                    file
                )[1]

                if (
                    extension
                    not in self.supported_extensions
                ):

                    continue

                file_path = os.path.join(
                    root,
                    file
                )

                if extension == ".py":

                    dependencies.extend(

                        self.analyze_python_file(
                            file_path,
                            project_path
                        )
                    )

                elif extension in {

                    ".ts",
                    ".js"
                }:

                    dependencies.extend(

                        self.analyze_ts_js_file(
                            file_path,
                            project_path
                        )
                    )

        return dependencies