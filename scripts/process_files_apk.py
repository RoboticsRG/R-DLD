# from androguard.core.bytecodes.apk import APK
from androguard.core.apk import APK
import os
"""
Esse script tem a funcao principal de verificar se a rotacao da tela esta bloqueada no aplicativo
Uma funcao secundaria e contar a quantidade de activities e quantas activities tem a opcao configChanges
"""


def list_apks_2(path):
    apps = []
    for name in os.listdir(path):
        file_name = os.path.join(path, name)
        if ".apk" in file_name:
            apps.append(file_name)
    return apps


def list_apks(path):
    # Inicializa uma lista vazia para armazenar os arquivos .apk encontrados
    apps = []

    # Usa os.walk para percorrer o diretório e suas subpastas
    for root, _, files in os.walk(path):
        # Percorre todos os arquivos encontrados
        for name in files:
            # Constrói o caminho completo do arquivo
            file_name = os.path.join(root, name)

            # Verifica se o arquivo tem a extensão .apk
            if file_name.endswith(".apk"):
                # Adiciona o caminho completo do arquivo à lista
                apps.append(file_name)

    # Retorna a lista de arquivos .apk encontrados
    return apps

def test_orientation_app(path):
    apk = APK(path)
    main_activity = apk.get_main_activity()
    activities = apk.get_activities()
    category = path.split('/')[-2]
    filename = path.split('/')[-1]
    screen_orientation = list(apk.get_all_attribute_value("activity", "screenOrientation", False))
    config_changes = list(apk.get_all_attribute_value("activity", "configChanges", False))
    rotation_main = apk.get_attribute_value('activity', 'screenOrientation', name=main_activity)
    rotation_other = apk.get_attribute_value('activity', 'screenOrientation')
    sdk_version = apk.get_target_sdk_version()
    return path, category, filename, main_activity, len(activities), len(screen_orientation), len(config_changes), rotation_main, rotation_other, sdk_version


def save_csv(path, name='screenOrientation_old4.csv'):
    """rotation_main = se tiver o valor none que dizer que a tela rotaciona. quaisquer outro valor a tela não rotaciona """
    list_app = list_apks(path)
    f = open(name, 'w')
    f.write('path;category;filename;main_activity;activities;screenOrientation;configChanges;rotation_main;rotation_other;sdk_version\n')
    for app_name in list_app:
        try:
            cat = test_orientation_app(app_name)
            f.write(f'{cat[0]};{cat[1]};{cat[2]};{cat[3]};{cat[4]};{cat[5]};{cat[6]};{cat[7]};{cat[8]};{cat[9]}\n')
        except:
            f.write(f'{app_name};err;err;err;err;err;err;err\n')
            print("erro:", app_name)

    f.close()


def list_activity_orientation(path):
    apk = APK(path)
    search = list(apk.get_all_attribute_value("activity", "screenOrientation"))
    activities = list(apk.get_all_attribute_value("activity", "name"))
    # activities = apk.get_activities()
    # activities = list(apk.get_all_attribute_value("activity", "screenOrientation", False))
    # test = apk.get_all_attribute_value("activity", "screenOrientation")
    print(apk.get_main_activity())
    print()
    main_activity_name = apk.get_main_activity()
    main_activity = apk.get_attribute_value('activity', 'screenOrientation', name=main_activity_name)
    other_activity = apk.get_attribute_value('activity', 'screenOrientation')
    print("main_activity:",main_activity)
    print("other_activity:", other_activity)
    # print(apk.get_target_sdk_version())
    print()
    for i in activities:
        print(i)
    # apk.
    print("screenOrientation:", len(search))
    for i in search:
        print("\t",i)


def main_activity_blocked(path):
    aux = test_orientation_app(path)[5]
    print(aux)
    if aux is None:
        return "main_activity_blocked: not"
    else:
        return "main_activity_blocked: yes"

# local para salvar o relatorio
name_save = '/home/swprojeto/projetos_git/files2024/teste/files_process.csv'
# pasta com arquivos apk separados por categorias
path_dir = '/home/swprojeto/projetos_git/files2024/teste/'
save_csv(path_dir, name_save)
