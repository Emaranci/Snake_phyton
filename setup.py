import cx_Freeze

executables = [cx_Freeze.Executable("SNAKE.py", base = "Win32GUI")]

build_exe_options = {"packages": ["pygame"],
                     "include_files":
                     ["icon.png","selva.png","Selva_inicio.png","selva_pause.png","dead-Song.ogg","Eat01-Song.ogg","Eat02-Song.ogg","Eat03-Song.ogg","snake_song.ogg"]}

cx_Freeze.setup(
    name = "SNAKE",
    version = "1.0", #27-08-2019
    description = "Primera version de replica de juego clasico SNAKE",
    options = {"build_exe": build_exe_options},
    executables = executables
    )


#Paja crear ejecutable ingresar a cmd y teclear "setup.py build"
