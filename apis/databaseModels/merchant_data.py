
from django.db import models

class merchant_data(models.Model):
    merchantId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    emailId = models.CharField(max_length=255, null=True, db_column='emilId')
    isEmailVerified = models.SmallIntegerField(null=True)
    isContactNumberVerified = models.SmallIntegerField(null=True)
    contactNumber = models.CharField(max_length=45,null=True)
    contactDesignation = models.CharField(max_length=100,null=True)
    aadharNumber = models.CharField(max_length=45,null=True)
    panCard = models.CharField(max_length=45,null=True)
    accountNumber = models.CharField(max_length=45, null=True)
    bankName = models.CharField(max_length=255, null=True)
    accountHolderName = models.CharField(max_length=255, null=True)
    ifscCode = models.CharField(max_length=45, null=True)
    companyName = models.CharField(max_length=255, null=True)
    companyLogoPath = models.CharField(max_length=255, null=True)
    companyImagePath = models.CharField(max_length=255, null=True)
    companyDescription = models.TextField(null=True)
    companyType = models.CharField(max_length=45, null=True)
    companyWebsite = models.CharField(max_length=255, null=True)
    clientName = models.CharField(max_length=255, null=True)
    clientCode = models.CharField(max_length=45, null=True)
    successUrl = models.CharField(max_length=255, null=True)
    failureUrl = models.CharField(max_length=255, null=True)
    
    ##added loginMasterId##
    loginMasterId = models.CharField(max_length=255, null=True)
    # loginMasterId = models.ForeignKey('api.login_master', on_delete=models.CASCADE, null=True, db_column='loginMasterId')
    created_date = models.DateTimeField(null=True)
    modifiedDate = models.DateTimeField(null=True, db_column='modified_date')
    modified_by = models.IntegerField(null=True)
    status = models.CharField(max_length=50, null=True, default = 'Pending')
    reason = models.CharField(max_length=255, null=True)
    businessType = models.CharField(max_length=45, null=True)
    yourRole = models.CharField(max_length=100, null=True)
    nameOnPanCard = models.CharField(max_length=200, null=True)
    registeredBusinessAdress = models.CharField(max_length=200, null=True)
    stateId = models.CharField(max_length=200, null=True)
    pinCode = models.CharField(max_length=100, null=True)
    
    registerdWithGST = models.BooleanField(null=True)
    gstNumber = models.CharField(max_length=100, null=True)
    monthlyRevenue = models.CharField(max_length=100, null=True)
    partnerBankId = models.CharField(max_length=100, null=True)
    
    mouAgreement = models.CharField(max_length=100, null=True)
    constitutionOfMerchant = models.CharField(max_length=200, null=True)
    addressProof = models.CharField(max_length=100, null=True)
    entityProof = models.CharField(max_length=200, null=True)
    utilityBill = models.CharField(max_length=250, null=True)
    panProof = models.CharField(max_length=250, null=True)
    kycOneProof = models.CharField(max_length=150, null=True)
    kycTwoProof = models.CharField(max_length=250, null=True)
    kycThreeProof = models.CharField(max_length=250, null=True)
    kycFourProof = models.CharField(max_length=250, null=True)
    kycFiveProof = models.CharField(max_length=250, null=True)
    bankLetter = models.CharField(max_length=250, null=True)
    onBoardFrom = models.CharField(max_length=200, null=True)
    requestId = models.CharField(max_length=250, null=True)
    clientType = models.CharField(max_length=250, null=True, db_column='client_type')
    parentClientId = models.CharField(max_length=250, null=True, db_column='parent_client_id')
    businessCategory = models.CharField(max_length=250, null=True)
    businessModel = models.CharField(max_length=250, null=True)
    billingLabel = models.CharField(max_length=250, null=True)
    erpCheck = models.CharField(max_length=250, null=True)
    platformId = models.CharField(max_length=250, null=True)
    collectionTypeId = models.CharField(max_length=100, null=True)
    collectionFrequencyId = models.CharField(max_length=100, null=True, db_column='collectionFrequencyeId')
    expectedTransactions = models.CharField(max_length=100, null=True, db_column='expectedTransaction')
    formBuild = models.CharField(max_length=100, null=True)
    ticketSize = models.CharField(max_length=100, null=True)
    signatoryPAN = models.CharField(max_length=250, null=True)
    cityId = models.CharField(max_length=100, null=True)
    operationalAddress = models.CharField(max_length=100, null=True)
    class Meta:
        db_table = 'merchant_data'
    
    
        