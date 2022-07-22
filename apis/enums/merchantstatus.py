from enum import Enum


class MerchantStatusCode(Enum):
    ACTIVATED = "Activated"
    DEACTIVATED = "Deactivated"
    BLOCKED = "Blocked"
    REJECTED = "Rejected"
    PENDING = "Pending"
    REQUESTED = "Requested"
    INCOMPLETE_KYC = "Incomplete KYC"
    APPROVED = "Approved"
    VERIFIED = "Verified"
    NOT_VERIFIED = "Not Verified"
    KYC_NOT_INITIATED = "KYC Not Initiated"
