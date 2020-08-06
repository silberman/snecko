CARDS = set(["A Thousand Cuts",
"A Thousand Cuts+1",
"Abandon",
"Abandon+1",
"AbeCurse",
"Accuracy",
"Accuracy+1",
"Acrobatics",
"Acrobatics+1",
"Adaptation",
"Adaptation+1",
"Adrenaline",
"Adrenaline+1",
"After Image",
"After Image+1",
"Aggregate",
"Aggregate+1",
"All For One",
"All For One+1",
"All Out Attack",
"All Out Attack+1",
"Alpha",
"Alpha+1",
"Amnesia",
"Amplify",
"Amplify+1",
"Anger",
"Anger+1",
"Apotheosis",
"Apotheosis+1",
"Armaments",
"Armaments+1",
"AscendersBane",
"Atom Bomb",
"Atom Bomb+1",
"Auto Shields",
"Auto Shields+1",
"AutoReboundSystem+1",
"Backflip",
"Backflip+1",
"Backstab",
"Backstab+1",
"Ball Lightning",
"Ball Lightning+1",
"Bandage Up",
"Bandage Up+1",
"Bane",
"Bane+1",
"Barrage",
"Barrage+1",
"Barricade",
"Barricade+1",
"Bash",
"Bash+1",
"BasicCrystalCard",
"BasicCrystalCard+1",
"Battery",
"Battle Trance",
"Battle Trance+1",
"BattleHymn",
"BattleHymn+1",
"Beam Cell",
"Beam Cell+1",
"Berserk",
"Berserk+1",
"Biased Cognition",
"Biased Cognition+1",
"BigBadWolf",
"Bite",
"Bite+1",
"Blade Dance",
"Blade Dance+1",
"Blasphemy",
"Blasphemy+1",
"Blind",
"Blind+1",
"Blizzard",
"Blizzard+1",
"Blood for Blood",
"Blood for Blood+1",
"BloodShelter+1",
"Bloodbath",
"Bloodletting",
"Bloodletting+1",
"Bloodthirsty+1",
"BloodyBrimstone",
"Bludgeon",
"Bludgeon+1",
"BlueStar",
"Blur",
"Blur+1",
"Body Slam",
"Body Slam+1",
"BootSequence",
"BootSequence+1",
"Bouncing Flask",
"Bouncing Flask+1",
"BowlingBash",
"BowlingBash+1",
"Brilliance",
"Brilliance+1",
"Brutality",
"Brutality+1",
"Buffer",
"Buffer+1",
"Bullet Time",
"Bullet Time+1",
"Burning Pact",
"Burning Pact+1",
"Burst",
"Burst+1",
"Calculated Gamble",
"Calculated Gamble+1",
"Caltrops",
"Caltrops+1",
"Candy+1",
"Capacitor",
"Capacitor+1",
"Carnage",
"Carnage+1",
"CarveReality",
"CarveReality+1",
"Catalyst",
"Catalyst+1",
"Chaos",
"Chaos+1",
"ChaoticCore+1",
"Chill",
"Chill+1",
"Choke",
"Choke+1",
"Chrysalis",
"Chrysalis+1",
"Clash",
"Clash+1",
"CleanseEvil",
"CleanseEvil+1",
"ClearTheMind",
"ClearTheMind+1",
"Cleave",
"Cleave+1",
"Cloak And Dagger",
"Cloak And Dagger+1",
"Clothesline",
"Clothesline+1",
"Clumsy",
"Cold Snap",
"Cold Snap+1",
"Collect",
"Collect+1",
"Combust",
"Combust+1",
"CommonCold",
"Compile Driver",
"Compile Driver+1",
"Concentrate",
"Concentrate+1",
"Conclude",
"Conclude+1",
"ConjureBlade",
"ConjureBlade+1",
"Consecrate",
"Consecrate+1",
"Conserve Battery",
"Conserve Battery+1",
"Consume",
"Consume+1",
"Coolheaded",
"Coolheaded+1",
"Core Surge",
"Core Surge+1",
"Corpse Explosion",
"Corpse Explosion+1",
"Corruption",
"Corruption+1",
"Creative AI",
"Creative AI+1",
"Crescendo",
"Crescendo+1",
"Crippling Poison",
"Crippling Poison+1",
"Crow Ritual",
"Crow Ritual+1",
"CrushJoints",
"CrushJoints+1",
"Crystallizer",
"Crystallizer+1",
"CurseOfTheBell",
"CutThroughFate",
"CutThroughFate+1",
"Dagger Spray",
"Dagger Spray+1",
"Dagger Throw",
"Dagger Throw+1",
"Dark Embrace",
"Dark Embrace+1",
"Dark Shackles",
"Dark Shackles+1",
"Darkness",
"Darkness+1",
"Dash",
"Dash+1",
"Deadly Poison",
"Deadly Poison+1",
"Decay",
"DeceiveReality",
"DeceiveReality+1",
"Deep Breath",
"Deep Breath+1",
"Defend_B",
"Defend_B+1",
"Defend_G",
"Defend_G+1",
"Defend_G+2",
"Defend_P",
"Defend_P+1",
"Defend_R",
"Defend_R+1",
"Defend_R+2",
"Deflect",
"Deflect+1",
"Defragment",
"Defragment+1",
"Defy Death",
"Defy Death+1",
"Delirium",
"Demon Form",
"Demon Form+1",
"Demonic Infusion",
"DeusExMachina",
"DeusExMachina+1",
"DevaForm",
"DevaForm+1",
"Devotion",
"Devotion+1",
"Die Die Die",
"Die Die Die+1",
"Disarm",
"Disarm+1",
"Discovery",
"Discovery+1",
"Distraction",
"Distraction+1",
"Dodge and Roll",
"Dodge and Roll+1",
"Doom and Gloom",
"Doom and Gloom+1",
"Doppelganger",
"Doppelganger+1",
"Double Energy",
"Double Energy+1",
"Double Tap",
"Double Tap+1",
"Doubt",
"Draining Mist",
"Draining Mist+1",
"Dramatic Entrance",
"Dramatic Entrance+1",
"Dream",
"Dropkick",
"Dropkick+1",
"Dual Strike",
"Dual Strike+1",
"Dual Wield",
"Dual Wield+1",
"Dualcast",
"Dualcast+1",
"Echo Form",
"Echo Form+1",
"Eclipse",
"Eclipse+1",
"Electrodynamics",
"Electrodynamics+1",
"EmptyBody",
"EmptyBody+1",
"EmptyFist",
"EmptyFist+1",
"EmptyMind",
"EmptyMind+1",
"Endless Agony",
"Endless Agony+1",
"Enlightenment",
"Enlightenment+1",
"Entrench",
"Entrench+1",
"Envenom",
"Envenom+1",
"Envy",
"Eruption",
"Eruption+1",
"Escape Plan",
"Escape Plan+1",
"Establishment",
"Establishment+1",
"Evaluate",
"Evaluate+1",
"Eviscerate",
"Eviscerate+1",
"Evolve",
"Evolve+1",
"Exhume",
"Exhume+1",
"Expertise",
"Expertise+1",
"FIFO Queue",
"FIFO Queue+1",
"FTL",
"FTL+1",
"Fasting",
"Fasting+1",
"Fasting2",
"Fasting2+1",
"FearNoEvil",
"FearNoEvil+1",
"Feed",
"Feed+1",
"Feel No Pain",
"Feel No Pain+1",
"Fiend Fire",
"Fiend Fire+1",
"FieryBird",
"Finesse",
"Finesse+1",
"Finisher",
"Finisher+1",
"Fire Breathing",
"Fire Breathing+1",
"Fission",
"Fission+1",
"Flame Barrier",
"Flame Barrier+1",
"Flash of Steel",
"Flash of Steel+1",
"Flechettes",
"Flechettes+1",
"Flex",
"Flex+1",
"FlowState",
"FlowState+1",
"Fluid Movement",
"Fluid Movement+1",
"FlurryOfBlows",
"FlurryOfBlows+1",
"Flying Knee",
"Flying Knee+1",
"FlyingSleeves",
"FlyingSleeves+1",
"FollowUp",
"FollowUp+1",
"Footwork",
"Footwork+1",
"Force Field",
"Force Field+1",
"ForeignInfluence",
"ForeignInfluence+1",
"Forethought",
"Forethought+1",
"Fusion",
"Fusion+1",
"GalaxyChild",
"Gash",
"Gash+1",
"Genetic Algorithm",
"Genetic Algorithm+1",
"GhostCostume+1",
"GhostWarHorse+1",
"Ghostly",
"Ghostly Armor",
"Ghostly Armor+1",
"Ghostly+1",
"Glacier",
"Glacier+1",
"Glass Knife",
"Glass Knife+1",
"Gluttony",
"Go for the Eyes",
"Go for the Eyes+1",
"Good Instincts",
"Good Instincts+1",
"Grand Finale",
"Grand Finale+1",
"Greed",
"GreedKing",
"Hallucinations",
"Halt",
"Halt+1",
"HandOfGreed",
"HandOfGreed+1",
"Hatred",
"Havoc",
"Havoc+1",
"Headbutt",
"Headbutt+1",
"Heatsinks",
"Heatsinks+1",
"Heavy Blade",
"Heavy Blade+1",
"Heel Hook",
"Heel Hook+1",
"Hello World",
"Hello World+1",
"Hemogenesis",
"Hemogenesis+1",
"Hemokinesis",
"Hemokinesis+1",
"Hidden Blade",
"Hidden Blade+1",
"Hologram",
"Hologram+1",
"Hyperbeam",
"Hyperbeam+1",
"Icecream+1",
"Immolate",
"Immolate+1",
"Impatience",
"Impatience+1",
"Impervious",
"Impervious+1",
"Indignation",
"Indignation+1",
"Infernal Blade",
"Infernal Blade+1",
"Infinite Blades",
"Infinite Blades+1",
"Inflame",
"Inflame+1",
"Injury",
"InnerPeace",
"InnerPeace+1",
"Intimidate",
"Intimidate+1",
"Intolerance",
"Iron Wave",
"Iron Wave+1",
"J.A.X.",
"J.A.X.+1",
"Jack Of All Trades",
"Jack Of All Trades+1",
"Judgement",
"Judgement+1",
"Juggernaut",
"Juggernaut+1",
"JustLucky",
"JustLucky+1",
"LackOfEnergy",
"Languid",
"Leap",
"Leap+1",
"Leg Sweep",
"Leg Sweep+1",
"LessonLearned",
"LessonLearned+1",
"Life Link",
"Life Link+1",
"LifeRuler+1",
"LikeWater",
"LikeWater+1",
"Limit Break",
"Limit Break+1",
"LimitFlipper+1",
"LittleHelper",
"Lockon",
"Lockon+1",
"Loop",
"Loop+1",
"Lust",
"Machine Learning",
"Machine Learning+1",
"Madness",
"Madness+1",
"Magnetism",
"Magnetism+1",
"Malaise",
"Malaise+1",
"Massacre",
"Massacre+1",
"Master of Strategy",
"Master of Strategy+1",
"MasterReality",
"MasterReality+1",
"Masterful Stab",
"Masterful Stab+1",
"Mayhem",
"Mayhem+1",
"Meditate",
"Meditate+1",
"Melter",
"Melter+1",
"MentalFortress",
"MentalFortress+1",
"Metallicize",
"Metallicize+1",
"Metamorphosis",
"Metamorphosis+1",
"Metaphysics",
"Metaphysics+1",
"Meteor Strike",
"Meteor Strike+1",
"Midas Touch",
"Midas Touch+1",
"Mind Blast",
"Mind Blast+1",
"Mirror Shield",
"Mirror Shield+1",
"Multi-Cast",
"Multi-Cast+1",
"Necronomicurse",
"Neutralize",
"Neutralize+1",
"Night Terror",
"Night Terror+1",
"Nirvana",
"Nirvana+1",
"Normality",
"Noxious Fumes",
"Noxious Fumes+1",
"Offering",
"Offering+1",
"Omniscience",
"Omniscience+1",
"Outmaneuver",
"Outmaneuver+1",
"Overencumbered",
"Pain",
"Panacea",
"Panacea+1",
"Panache",
"Panache+1",
"Panic Button",
"Panic Button+1",
"PanicButton",
"PanicButton+1",
"Parasite",
"PathToVictory",
"PathToVictory+1",
"PatternShift",
"PerfectCombo",
"Perfected Strike",
"Perfected Strike+1",
"Perseverance",
"Perseverance+1",
"Phantasmal Killer",
"Phantasmal Killer+1",
"PiercingWail",
"PiercingWail+1",
"Poison Darts",
"Poisoned Stab",
"Poisoned Stab+1",
"Poisoned Strike+1",
"Pommel Strike",
"Pommel Strike+1",
"Porccubus",
"Pot Of Greed",
"Pot Of Greed+1",
"Power Through",
"Power Through+1",
"Pray",
"Pray+1",
"Predator",
"Predator+1",
"Prepared",
"Prepared+1",
"Pride",
"Prostrate",
"Prostrate+1",
"Protect",
"Protect+1",
"Provocation",
"Provocation+1",
"Pulse",
"Pulse+1",
"PulseDistributor",
"PulseMagic+1",
"Pummel",
"Pummel+1",
"Purity",
"Purity+1",
"Quick Slash",
"Quick Slash+1",
"RabbitOfFibonacci+3",
"Rage",
"Rage+1",
"Ragnarok",
"Ragnarok+1",
"Rainbow",
"Rainbow+1",
"Rampage",
"Rampage+1",
"ReachHeaven",
"ReachHeaven+1",
"Reaper",
"Reaper+1",
"Reboot",
"Reboot+1",
"Rebound",
"Rebound+1",
"Reckless Charge",
"Reckless Charge+1",
"Recycle",
"Recycle+1",
"Redo",
"Redo+1",
"Reflect",
"Reflect+1",
"Reflex",
"Reflex+1",
"Regret",
"Reinforced Body",
"Reinforced Body+1",
"Reprogram",
"Reprogram+1",
"Riddle With Holes",
"Riddle With Holes+1",
"Rip and Tear",
"Rip and Tear+1",
"RitualDagger",
"RitualDagger+1",
"Run Through",
"Run Through+1",
"Rupture",
"Rupture+1",
"Sadistic Nature",
"Sadistic Nature+1",
"Sanctity",
"Sanctity+1",
"SandsOfTime",
"SandsOfTime+1",
"SashWhip",
"SashWhip+1",
"Scarecrow",
"Scorched",
"Scrape",
"Scrape+1",
"Scrawl",
"Scrawl+1",
"Searing Blow",
"Searing Blow+1",
"Searing Blow+10",
"Searing Blow+11",
"Searing Blow+12",
"Searing Blow+13",
"Searing Blow+14",
"Searing Blow+15",
"Searing Blow+15",
"Searing Blow+16",
"Searing Blow+17",
"Searing Blow+18",
"Searing Blow+19",
"Searing Blow+2",
"Searing Blow+20",
"Searing Blow+21",
"Searing Blow+22",
"Searing Blow+23",
"Searing Blow+24",
"Searing Blow+25",
"Searing Blow+26",
"Searing Blow+27",
"Searing Blow+28",
"Searing Blow+29",
"Searing Blow+3",
"Searing Blow+4",
"Searing Blow+5",
"Searing Blow+6",
"Searing Blow+7",
"Searing Blow+8",
"Searing Blow+9",
"Second Wind",
"Second Wind+1",
"Secret Technique",
"Secret Technique+1",
"Secret Weapon",
"Secret Weapon+1",
"Seeing Red",
"Seeing Red+1",
"Seek",
"Seek+1",
"Self Repair",
"Self Repair+1",
"Sentinel",
"Sentinel+1",
"Setup",
"Setup+1",
"Sever Soul",
"Sever Soul+1",
"Shame",
"Sharp Hide",
"Shiv",
"Shockwave",
"Shockwave+1",
"Shrug It Off",
"Shrug It Off+1",
"SignatureMove",
"SignatureMove+1",
"SingingMachine",
"Skewer",
"Skewer+1",
"Skim",
"Skim+1",
"Slice",
"Slice+1",
"Sloth",
"Sneak Up",
"Sneak Up+1",
"Specialist",
"Specialist+1",
"SpiderBud",
"SpiritShield",
"SpiritShield+1",
"Spot Weakness",
"Spot Weakness+1",
"Stack",
"Stack+1",
"Static Discharge",
"Static Discharge+1",
"Steam",
"Steam Power",
"Steam Power+1",
"Steam+1",
"StepAndStrike",
"StepAndStrike+1",
"Storm",
"Storm of Steel",
"Storm of Steel+1",
"Storm+1",
"Streamline",
"Streamline+1",
"Strike_B",
"Strike_B+1",
"Strike_G",
"Strike_G+1",
"Strike_P",
"Strike_P+1",
"Strike_R",
"Strike_R+1",
"Strike_R+3",
"Study",
"Study+1",
"Sucker Punch",
"Sucker Punch+1",
"Sunder",
"Sunder+1",
"Survey Options",
"Survivor",
"Survivor+1",
"Sweeping Beam",
"Sweeping Beam+1",
"Swift Strike",
"Swift Strike+1",
"Swivel",
"Swivel+1",
"Sword Boomerang",
"Sword Boomerang+1",
"SwordBurial+1",
"Tactician",
"Tactician+1",
"TalkToTheHand",
"TalkToTheHand+1",
"Tantrum",
"Tantrum+1",
"Tempest",
"Tempest+1",
"Terror",
"Terror+1",
"The Bomb",
"The Bomb+1",
"Thinking Ahead",
"Thinking Ahead+1",
"ThirdEye",
"ThirdEye+1",
"Thunder Strike",
"Thunder Strike+1",
"Thunderclap",
"Thunderclap+1",
"Time Bomb",
"Time Bomb+1",
"Tools of the Trade",
"Tools of the Trade+1",
"Toxin Wave",
"Toxin Wave+1",
"Transmutation",
"Transmutation+1",
"Trick",
"Trick+1",
"Trip",
"Trip+1",
"True Grit",
"True Grit+1",
"Turbo",
"Turbo+1",
"Twin Strike",
"Twin Strike+1",
"Underhanded Strike",
"Underhanded Strike+1",
"Undo",
"Undo+1",
"Unload",
"Unload+1",
"Unraveling",
"Uppercut",
"Uppercut+1",
"Vault",
"Vault+1",
"Vengeance",
"Vengeance+1",
"Venomology",
"Venomology+1",
"Vigilance",
"Vigilance+1",
"Violence",
"Violence+1",
"Voices",
"Wallop",
"Wallop+1",
"Warcry",
"Warcry+1",
"WaveOfTheHand",
"WaveOfTheHand+1",
"WeaponsOverheat",
"WeaponsOverheat+1",
"Weave",
"Weave+1",
"Well Laid Plans",
"Well Laid Plans+1",
"Wellcheers",
"WheelKick",
"WheelKick+1",
"Whirlwind",
"Whirlwind+1",
"White Noise",
"White Noise+1",
"Wild Strike",
"Wild Strike+1",
"WindmillStrike",
"WindmillStrike+1",
"Wireheading",
"Wireheading+1",
"Wish",
"Wish+1",
"Worship",
"Worship+1",
"Wraith Form v2",
"Wraith Form v2+1",
"Wrath",
"WreathOfFlame",
"WreathOfFlame+1",
"Writhe",
"Zap",
"Zap+1",
])
