from tikets import Tikets
from managers import Managers
import schedule
import time

tikets = Tikets()
members = Managers()

def check_labels(tiket):
    labels_flag = False
    for label in tiket['labels']:
        if tikets.is_need_assign_label(label["name"]):
            labels_flag = True
            break
    return labels_flag


def check_members(tiket):
    members_flag = True
    for idMember in tiket["idMembers"]:
        if members.is_need_assign_managers(idMember):
            pass
        else:
            members_flag = False
            break
    return members_flag


def check_conditions(members_flag, labels, tiket):
    if labels and members_flag:
        if len(members.current_list) > 0:
            members.assign_manage(tiket["id"])
            return "Assign"
        else:
            members.restore_list()
            members.update_current_list()
            members.assign_manage(tiket["id"])
            return "Assign"
    else:
        return "Not assign"


def assign_if_nead():
    members.update_current_list()
    for tiket in tikets.get_tikets():
        print(check_conditions(check_members(tiket), check_labels(tiket), tiket))


schedule.every(5).seconds.do(assign_if_nead)


while True:
    try:
        schedule.run_pending()
    except:
        print("Something went wrong")
        schedule.run_pending()

