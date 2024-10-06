from corecalc.stats import MetsSpeedStats


class SpeedSkatingStats(MetsSpeedStats):
    """
    Statistics for a walking exercise.

    - source:
        https://cdn-links.lww.com/permalink/mss/a/mss_43_8_2011_06_13_ainsworth_202093_sdc1.pdf

    I combined the roller blading, ice skating and speed skating values:
        - Ice skating: 5.5 METs and 14.48 km/h, which is 7.5 METs for roller
          blading.
        - For roller blading, 17.7 km/h results in 9.8 METs. Assuming that
          ice skating is the same at low speeds as speed skating, and that ice
          skating scaler linearly with roller blading, I assumed that the speed
          skating values is 7.8 METs and 17.7 km/h.
        - Doing the same for roller blading at 21.0 km/h (12.3 METs) which is
          10.3 METs for speed skating.
        - Doing the same for roller blading at 24.0 km/h (14.0 METs) which is
          12.0 METs for speed skating.
        - Competitive speed skating is has a METs value of 13.3 METs, which is
          can be interpolated to
    """

    METS_KCAL_KG_H = 5.5, 7.8, 10.3, 12.0, 13.3
    METS_KM_H = 14.48, 17.7, 21.0, 24.0, 26.6
