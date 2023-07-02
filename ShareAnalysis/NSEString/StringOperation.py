class StringOperation(object):
    """This class will handle string operation"""

    def splitNSEStringWithNewLineSeparator(self, nseStringValue):
        nseStringValue = nseStringValue.strip()
        return nseStringValue.splitlines()


    def splitNSEStringWithCommaSeparator(self, nseStringValue):
        nseStringValue = nseStringValue.strip()
        return nseStringValue.split(",")