import random
names = [
    '007',
    'Advantage',
    'Alert',
    'Backhander',
    'Blade',
    'Blaze',
    'Blockade',
    'Blockbuster',
    'Boxer',
    'Brimstone',
    'Broadway',
    'Buccaneer',
    'Champion',
    'Cliffhanger',
    'Coachman',
    'Comet',
    'Commander',
    'Courier',
    'Cowboy',
    'Crawler',
    'Crossroads',
    'Deep Space',
    'Desperado',
    'Double-Decker',
    'Echelon',
    'Edge',
    'Encore',
    'En Route',
    'Escape',
    'Eureka',
    'Evangelist',
    'Excursion',
    'Explorer',
    'Fantastic',
    'Firefight',
    'Foray',
    'Forge',
    'Freeway',
    'Fun Machine',
    'Game Over',
    'Genesis',
    'Hacker',
    'Hawkeye',
    'Haybailer',
    'Haystack',
    'Hexagon',
    'Hitman',
    'Hustler',
    'Iceberg',
    'Impulse',
    'Invader',
    'Inventor',
    'Iron Wolf',
    'Jackrabbit',
    'Juniper',
    'Keyhole',
    'Lancelot',
    'Mad Hatter',
    'Magnum',
    'Majestic',
    'Merlin',
    'Multiplier',
    'Netiquette',
    'Nomad',
    'Octagon',
    'Offense',
    'Olive Branch',
    'Olympic Torch',
    'Omega',
    'Onyx',
    'Orbit',
    'Outer Space',
    'Outlaw',
    'Patron',
    'Patriot',
    'Pegasus',
    'Pentagon',
    'Pilgrim',
    'Pinball',
    'Pinnacle',
    'Pipeline',
    'Pirate',
    'Pirate Ship',
    'Portal',
    'Predator',
    'Prism',
    'Raging Bull',
    'Ragtime',
    'Reunion',
    'Ricochet',
    'Roadrunner',
    'Robin Hood',
    'Rover',
    'Runabout',
    'Sapphire',
    'Scrappy',
    'Seige',
    'Shadow',
    'Shakedown',
    'Shockwave',
    'Shooter',
    'Showdown',
    'Six Pack',
    'Slam Dunk',
    'Slasher',
    'Sledgehammer',
    'Spirit',
    'Spotlight',
    'Starlight',
    'Steamroller',
    'Stride',
    'Sunrise',
    'Super Bowl',
    'Sunset',
    'Sweetheart',
    'Top Hand',
    'Touchdown',
    'Tour',
    'Trailblazer',
    'Transit',
    'Trecker (Trekker)',
    'Trio',
    'Triple Play',
    'Triple Threat',
    'Universe',
    'Unstoppable',
    'Utopia',
    'Vicinity',
    'Vector',
    'Vigilance',
    'Vigilante',
    'Vista',
    'Visage',
    'Vis-à-vis',
    'VIP',
    'Volley',
    'Whizzler',
    'Wingman'
]


def get_random_name():
    i = random.randint(1, len(names)-1)
    return names[i]
