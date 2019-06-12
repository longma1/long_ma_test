class InvalidVersionStringError(Exception):
    """
    Custom Exception to declare the version strings are invalid
    """
    pass


class Solution:
    def version_to_tuple(self, version: str):
        """
        Converts version string to list of integers

        :param version: a version tring, this function accepts any number of period separated version strings, can
                        be as long as an ip address and this will still work
        :return: a list of integers, representing the version string
        """
        r = []
        try:
            l = version.split('.')
            for i in l:
                r.append(int(i))
            return r
        except Exception as e:
            raise InvalidVersionStringError

    def version_compare(self, str1: str, str2: str):
        """
        Calls version_to_tuple to convert the version string to list of integers and compares the two version strings

        :param str1: version string 1 that is expected to have the same number of periods as version string 2
        :param str2: version string 1 that is expected to have the same number of periods as version string 2
        :return: a string stating which version string is greater/ if the two version strings are equal
        """
        try:
            ver1 = self.version_to_tuple(str1)
            ver2 = self.version_to_tuple(str2)
        except:
            raise InvalidVersionStringError('Invalid version strings')

        if len(ver1) != len(ver2):
            return InvalidVersionStringError('Inalid version strings')

        for i in range(len(ver1)):
            if ver1[i]>ver2[i]:
                return '"{}" is greater than "{}"'.format(str1, str2)
            elif ver2[i]>ver1[i]:
                return '"{}" is greater than "{}"'.format(str2, str1)
        return "The two version strings are equal"


