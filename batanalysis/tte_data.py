"""
This file holds the BAT TimeTaggedEvents class

Tyler Parsotan Jul 16 2024
"""
from .batlib import decompose_det_id


class TimeTaggedEvents(object):
    """
    This class encapsulates the event data that is obtained by the BAT instrument.

    TODO: add methods to add/concatenate event data, plot event data, etc
    """

    def __init__(
            self,
            times,
            detector_id,
            detx,
            dety,
            quality_flag,
            energy,
            pulse_height_amplitude,
            pulse_invariant,
            mask_weight=None,
    ):
        """
        This initalizes the TimeTaggedEvent class and allows for event data to be accessed easily.

        All attributes must be initalized and kept together here. They should all be astropy Quantity arrays with the
        units appropriately set for each quantity. This should be taken care of by the user.

        :param times: The MET times of each measured photon
        :param detector_id: The detector ID where each photon was measured
        :param detx: The detector X pixel where the photon was measured
        :param dety: The detector Y pixel where the photon was measured
        :param quality_flag: The quality flag for each measured photon
        :param energy: The gain/offset corrected energy of each measured photon
        :param pulse_height_amplitude: The pulse height amplitude of each measured photon
        :param pulse_invariant: The pulse invariant of each measured photon
        :param mask_weight: The mask weighting that may apply to each photon. Can be set to None to ignore mask weighting
        """

        self.time = times
        self.detector_id = detector_id
        self.detx = detx
        self.dety = dety
        self.quality_flag = quality_flag
        self.energy = energy
        self.pha = pulse_height_amplitude
        self.pi = pulse_invariant
        self.mask_weight = mask_weight

        # get the block/DM/sandwich/channel info
        block, dm, side, channel = decompose_det_id(self.detector_id)
        self.detector_block = block
        self.detector_dm = dm
        self.detector_sand = side
        self.detector_chan = channel
