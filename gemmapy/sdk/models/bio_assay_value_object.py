# coding: utf-8

"""
    Gemma RESTful API

    This website documents the usage of the [Gemma REST API](https://gemma.msl.ubc.ca/rest/v2/). Here you can find example script usage of the API, as well as graphical interface for each endpoint, with description of its parameters and the endpoint URL.  The documentation of the underlying java code can be found [here](https://gemma.msl.ubc.ca/resources/apidocs/ubic/gemma/web/services/rest/package-summary.html). See the [links section](https://gemma.msl.ubc.ca/resources/restapidocs/#footer) in the footer of this page for other relevant links.  Use of this webpage and Gemma web services, including the REST API, is subject to [these terms and conditions](https://pavlidislab.github.io/Gemma/terms.html). Please read these in full before continuing to use this webpage or any other part of the Gemma system.   # noqa: E501

    OpenAPI spec version: 2.4.1
    Contact: pavlab-support@msl.ubc.ca
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BioAssayValueObject(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'accession': 'DatabaseEntryValueObject',
        'array_design': 'ArrayDesignValueObject',
        'description': 'str',
        'metadata': 'str',
        'name': 'str',
        'original_platform': 'ArrayDesignValueObject',
        'outlier': 'bool',
        'predicted_outlier': 'bool',
        'processing_date': 'datetime',
        'sample': 'BioMaterialValueObject',
        'sequence_paired_reads': 'bool',
        'sequence_read_count': 'int',
        'sequence_read_length': 'int',
        'user_flagged_outlier': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'accession': 'accession',
        'array_design': 'arrayDesign',
        'description': 'description',
        'metadata': 'metadata',
        'name': 'name',
        'original_platform': 'originalPlatform',
        'outlier': 'outlier',
        'predicted_outlier': 'predictedOutlier',
        'processing_date': 'processingDate',
        'sample': 'sample',
        'sequence_paired_reads': 'sequencePairedReads',
        'sequence_read_count': 'sequenceReadCount',
        'sequence_read_length': 'sequenceReadLength',
        'user_flagged_outlier': 'userFlaggedOutlier'
    }

    def __init__(self, id=None, accession=None, array_design=None, description=None, metadata=None, name=None, original_platform=None, outlier=None, predicted_outlier=None, processing_date=None, sample=None, sequence_paired_reads=None, sequence_read_count=None, sequence_read_length=None, user_flagged_outlier=None):  # noqa: E501
        """BioAssayValueObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._accession = None
        self._array_design = None
        self._description = None
        self._metadata = None
        self._name = None
        self._original_platform = None
        self._outlier = None
        self._predicted_outlier = None
        self._processing_date = None
        self._sample = None
        self._sequence_paired_reads = None
        self._sequence_read_count = None
        self._sequence_read_length = None
        self._user_flagged_outlier = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if accession is not None:
            self.accession = accession
        if array_design is not None:
            self.array_design = array_design
        if description is not None:
            self.description = description
        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if original_platform is not None:
            self.original_platform = original_platform
        if outlier is not None:
            self.outlier = outlier
        if predicted_outlier is not None:
            self.predicted_outlier = predicted_outlier
        if processing_date is not None:
            self.processing_date = processing_date
        if sample is not None:
            self.sample = sample
        if sequence_paired_reads is not None:
            self.sequence_paired_reads = sequence_paired_reads
        if sequence_read_count is not None:
            self.sequence_read_count = sequence_read_count
        if sequence_read_length is not None:
            self.sequence_read_length = sequence_read_length
        if user_flagged_outlier is not None:
            self.user_flagged_outlier = user_flagged_outlier

    @property
    def id(self):
        """Gets the id of this BioAssayValueObject.  # noqa: E501


        :return: The id of this BioAssayValueObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BioAssayValueObject.


        :param id: The id of this BioAssayValueObject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def accession(self):
        """Gets the accession of this BioAssayValueObject.  # noqa: E501


        :return: The accession of this BioAssayValueObject.  # noqa: E501
        :rtype: DatabaseEntryValueObject
        """
        return self._accession

    @accession.setter
    def accession(self, accession):
        """Sets the accession of this BioAssayValueObject.


        :param accession: The accession of this BioAssayValueObject.  # noqa: E501
        :type: DatabaseEntryValueObject
        """

        self._accession = accession

    @property
    def array_design(self):
        """Gets the array_design of this BioAssayValueObject.  # noqa: E501


        :return: The array_design of this BioAssayValueObject.  # noqa: E501
        :rtype: ArrayDesignValueObject
        """
        return self._array_design

    @array_design.setter
    def array_design(self, array_design):
        """Sets the array_design of this BioAssayValueObject.


        :param array_design: The array_design of this BioAssayValueObject.  # noqa: E501
        :type: ArrayDesignValueObject
        """

        self._array_design = array_design

    @property
    def description(self):
        """Gets the description of this BioAssayValueObject.  # noqa: E501


        :return: The description of this BioAssayValueObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BioAssayValueObject.


        :param description: The description of this BioAssayValueObject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def metadata(self):
        """Gets the metadata of this BioAssayValueObject.  # noqa: E501


        :return: The metadata of this BioAssayValueObject.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this BioAssayValueObject.


        :param metadata: The metadata of this BioAssayValueObject.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this BioAssayValueObject.  # noqa: E501


        :return: The name of this BioAssayValueObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BioAssayValueObject.


        :param name: The name of this BioAssayValueObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def original_platform(self):
        """Gets the original_platform of this BioAssayValueObject.  # noqa: E501


        :return: The original_platform of this BioAssayValueObject.  # noqa: E501
        :rtype: ArrayDesignValueObject
        """
        return self._original_platform

    @original_platform.setter
    def original_platform(self, original_platform):
        """Sets the original_platform of this BioAssayValueObject.


        :param original_platform: The original_platform of this BioAssayValueObject.  # noqa: E501
        :type: ArrayDesignValueObject
        """

        self._original_platform = original_platform

    @property
    def outlier(self):
        """Gets the outlier of this BioAssayValueObject.  # noqa: E501


        :return: The outlier of this BioAssayValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._outlier

    @outlier.setter
    def outlier(self, outlier):
        """Sets the outlier of this BioAssayValueObject.


        :param outlier: The outlier of this BioAssayValueObject.  # noqa: E501
        :type: bool
        """

        self._outlier = outlier

    @property
    def predicted_outlier(self):
        """Gets the predicted_outlier of this BioAssayValueObject.  # noqa: E501


        :return: The predicted_outlier of this BioAssayValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._predicted_outlier

    @predicted_outlier.setter
    def predicted_outlier(self, predicted_outlier):
        """Sets the predicted_outlier of this BioAssayValueObject.


        :param predicted_outlier: The predicted_outlier of this BioAssayValueObject.  # noqa: E501
        :type: bool
        """

        self._predicted_outlier = predicted_outlier

    @property
    def processing_date(self):
        """Gets the processing_date of this BioAssayValueObject.  # noqa: E501


        :return: The processing_date of this BioAssayValueObject.  # noqa: E501
        :rtype: datetime
        """
        return self._processing_date

    @processing_date.setter
    def processing_date(self, processing_date):
        """Sets the processing_date of this BioAssayValueObject.


        :param processing_date: The processing_date of this BioAssayValueObject.  # noqa: E501
        :type: datetime
        """

        self._processing_date = processing_date

    @property
    def sample(self):
        """Gets the sample of this BioAssayValueObject.  # noqa: E501


        :return: The sample of this BioAssayValueObject.  # noqa: E501
        :rtype: BioMaterialValueObject
        """
        return self._sample

    @sample.setter
    def sample(self, sample):
        """Sets the sample of this BioAssayValueObject.


        :param sample: The sample of this BioAssayValueObject.  # noqa: E501
        :type: BioMaterialValueObject
        """

        self._sample = sample

    @property
    def sequence_paired_reads(self):
        """Gets the sequence_paired_reads of this BioAssayValueObject.  # noqa: E501


        :return: The sequence_paired_reads of this BioAssayValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._sequence_paired_reads

    @sequence_paired_reads.setter
    def sequence_paired_reads(self, sequence_paired_reads):
        """Sets the sequence_paired_reads of this BioAssayValueObject.


        :param sequence_paired_reads: The sequence_paired_reads of this BioAssayValueObject.  # noqa: E501
        :type: bool
        """

        self._sequence_paired_reads = sequence_paired_reads

    @property
    def sequence_read_count(self):
        """Gets the sequence_read_count of this BioAssayValueObject.  # noqa: E501


        :return: The sequence_read_count of this BioAssayValueObject.  # noqa: E501
        :rtype: int
        """
        return self._sequence_read_count

    @sequence_read_count.setter
    def sequence_read_count(self, sequence_read_count):
        """Sets the sequence_read_count of this BioAssayValueObject.


        :param sequence_read_count: The sequence_read_count of this BioAssayValueObject.  # noqa: E501
        :type: int
        """

        self._sequence_read_count = sequence_read_count

    @property
    def sequence_read_length(self):
        """Gets the sequence_read_length of this BioAssayValueObject.  # noqa: E501


        :return: The sequence_read_length of this BioAssayValueObject.  # noqa: E501
        :rtype: int
        """
        return self._sequence_read_length

    @sequence_read_length.setter
    def sequence_read_length(self, sequence_read_length):
        """Sets the sequence_read_length of this BioAssayValueObject.


        :param sequence_read_length: The sequence_read_length of this BioAssayValueObject.  # noqa: E501
        :type: int
        """

        self._sequence_read_length = sequence_read_length

    @property
    def user_flagged_outlier(self):
        """Gets the user_flagged_outlier of this BioAssayValueObject.  # noqa: E501


        :return: The user_flagged_outlier of this BioAssayValueObject.  # noqa: E501
        :rtype: bool
        """
        return self._user_flagged_outlier

    @user_flagged_outlier.setter
    def user_flagged_outlier(self, user_flagged_outlier):
        """Sets the user_flagged_outlier of this BioAssayValueObject.


        :param user_flagged_outlier: The user_flagged_outlier of this BioAssayValueObject.  # noqa: E501
        :type: bool
        """

        self._user_flagged_outlier = user_flagged_outlier

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BioAssayValueObject, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BioAssayValueObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
