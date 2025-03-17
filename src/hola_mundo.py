'''
    First Action
'''

#=====================#
# ---- Libraries ---- #
#=====================#

import os

#==========================#
# ---- Main Functions ---- #
#==========================#

def main():
    name = os.get_env("USERNAME")
    print(f'Hola {name} desde github!!')

if __name__ == '__main__':
    main()