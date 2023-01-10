from tikets import Tikets
from managers import Managers
import time

tikets = Tikets()
members = Managers()

while True:
    tikets.get_tikets()
    members.update_current_list()
    for tiket in tikets.get_tikets():
        label_flag = False
        manage_flag = True
        for label in tiket['labels']:
            if tikets.is_need_assign_label(label["name"]):
                label_flag = True
                break
        for idMember in tiket["idMembers"]:
            if members.is_need_assign_managers(idMember):
                pass
            else:
                manage_flag = False
                break
        if label_flag and manage_flag:
            if len(members.current_list) > 0:
                members.assign_manage(tiket["id"])
                print("Assign")
            else:
                members.restore_list()
                members.update_current_list()
                members.assign_manage(tiket["id"])
                print("Assign")

        else:
            print("Not assign")
    print(members.current_list)
    time.sleep(5)













