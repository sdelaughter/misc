"""
Calendar Fact Generator
Based on XKCD #1930
https://xkcd.com/1930/

Author: Samuel DeLaughter
License: MIT
Last Updated: 12/18/2017

Accepts an optional integer command line argument to generate a set number of facts.
Otherwise it will continue to generate them until you tell it to stop.
"""

import random
import sys


def build_options():
    g = [[], [], [], []]
    
    for i in ['Fall', 'Spring']:
        g[0].append('the {} Equinox'.format(i))
    for i in ['Winter', 'Summer']:
        for j in ['Solstice', 'Olympics']:
            g[0].append('the {} {}'.format(i, j))
    for i in ['earliest', 'latest']:
        for j in ['sunrise', 'sunset']: 
            g[0].append('the {} {}'.format(i, j))
    for i in ['Saving', 'Savings']:
        g[0].append('Daylight {} Time'.format(i))
    for i in ['Day', 'Year']:
        g[0].append('Leap {}'.format(i))
    g[0].append('Easter')
    for i in ['Harvest', 'Super', 'Blood']:
        g[0].append('the {} Moon'.format(i))
    g[0].append('Toyota Truck Month')
    g[0].append('Shark Week') 
    
    for i in ['earlier', 'later', 'at the wrong time']:
        g[1].append('happens {} every year'.format(i))
    cal = ['Sun', 'Moon', 'Zodiac', 'atomic clock in Colorado']
    for i in ['Gregorian', 'Mayan', 'Lunar', 'iPhone']:
        cal.append('{} calendar'.format(i))
    for i in cal:
        g[1].append('drifts out of sync with the {}'.format(i))
    for i in ['not happen', 'happen twice']:
        g[1].append('might {} this year'.format(i))    
    for i in ['Indiana', 'Arizona', 'Russia']:
        g[2].append('Time Zone legislation in {}'.format(i))
    g[2].append('a decree by the Pope in the 1500s')
    for i in ['precession', 'libration', 'nutation', 'libation', 'eccentricity', 'obliquity']:
        for j in ['Moon', 'Sun', "Earth's axis", 'Equator', 'Prime Meridian', 'International Date Line', 'Mason-Dixon Line']:
            g[2].append('{} of the {}'.format(i, j))
    g[2].append('magnetic field reversal')
    for i in['Benjamin Franklin', 'Isaac Newton', 'FDR']:
        g[2].append('an arbitraty decision by {}'.format(i))
    
    g[3].append('it causes a predictable increase in car accidents')
    g[3].append("that's why we have leap seconds")
    g[3].append('scientists are really worried')
    for i in ['Bronze Age', 'Ice Age', 'Cretaceous', '1990s']:
        g[3].append('it was even more extreme during the {}'.format(i))
    for i in ['will never happen', 'actually makes things worse', 'is stalled in Congress', 'might be unconstitutional']:
        g[3].append("there's a proposal to fix it, but it {}".format(i))
    g[3].append("it's getting worsea and no one knows why")

    return g


def get_fact(g):
    g0 = random.choice(g[0])
    g1 = random.choice(g[1])
    g2 = random.choice(g[2])
    g3 = random.choice(g[3])
    fact = 'Did you know that {} {} because of {}?  Apparently {}.'.format(g0, g1, g2, g3)
    return(fact)

    
def main():
    g = build_options()
    
    if len(sys.argv) > 1:
        for i in range(max(1, int(sys.argv[1]))):
            print(get_fact(g))
            print('\n')
    
    else:
        another = True
        while another:
            print('\n')
            print(get_fact(g))
            print('\n')
            c = raw_input("Want another calendar fact? (Y/n)\n")
            if c.upper() in ['N', 'NO', 'Q', 'QUIT']:
                another = False
    
    
if __name__ == "__main__": 
    main()
