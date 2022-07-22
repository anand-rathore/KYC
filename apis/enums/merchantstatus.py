from enum import Enum

class MerchantStatusCode(Enum):
    activated = "Activate"
    deactivated = "Deactivate"
    blocked = "Blocked"
    reject = "Rejected"
    pending = "Pending"
    requested = "Requested"
    incomplete_KYC = "Incompleted KYC"
    approved  = "Approved"
    verified = "Verified"
    not_Verified = "Not Verified"
    KYC_not_initiated= "KYC Not Initiated"