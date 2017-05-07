# @---wufeng---

from core.auth import login_required
from core.atm import select_party
from core.transaction_handle import transaction_handle


@login_required
def pay(userdata,usertype,txdesc,amount):
    """
    结算接口
    :return: 
    """
    party_id = select_party(userdata['userid'], 'payment')
    transaction_handle(party_id, 'payment', amount, '支付' + txdesc )
    return True