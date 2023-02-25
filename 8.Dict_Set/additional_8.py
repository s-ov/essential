text = """
The Battle of Vrbanja Bridge was an armed confrontation which took place on 27 May 1995, between United Nations (UN) 
peacekeepers from the French Army and elements of the Bosnian Serb Army of Republika Srpska (VRS). The fighting occurred
 at the Vrbanja Bridge crossing of the Miljacka river in Sarajevo, Bosnia and Herzegovina, during the Bosnian War. 
 The VRS seized the French-manned United Nations Protection Force (UNPROFOR) observation posts on both ends of the 
 bridge, taking twelve French peacekeepers hostage. Ten were taken away, and two were kept at the bridge as human 
 shields.
A platoon of 30 French peacekeepers led by Captain François Lecointre re-captured the bridge with the support of 70 
French infantrymen and direct fire from armoured vehicles. During the French assault, elements of the Army of the 
Republic of Bosnia and Herzegovina (ARBiH) opened fire on the VRS-held observation posts on their own initiative, 
accidentally wounding one French hostage. Two French soldiers were killed during the battle, and 17 were wounded. 
The VRS casualties were four killed, several wounded and four captured. Following the battle, VRS forces were observed
 to be less likely to engage French UN peacekeepers deployed in the city. In 2017, Lecointre, now an army general, was 
 appointed French Chief of the Defence Staff.
 The first evidence the French UN troops received that something was wrong at the Vrbanja Bridge was radio silence from 
 the French post. About 05:20, the company commander, Captain François Lecointre, unable to make radio contact with the 
 posts, drove to the bridge to find out what was happening.[12] He was met by a Serb sentry in French uniform who 
 attempted to take him prisoner. Lecointre quickly turned around and drove to Skenderija stadium, the headquarters of 
 FREBAT4.[2] When news of the takeover of the bridge reached the newly elected French President, Jacques Chirac, he 
 circumvented the UN chain of command and ordered an assault to retake the bridge from the Bosnian Serbs.[9]
The French command in Bosnia-Herzegovina responded by sending a platoon of 30 FREBAT4 troops from the 3rd Marine 
Infantry Regiment to re-capture the northern end of the bridge, backed by another 70 French infantry, six ERC 90 Sagaie 
armoured cars and several VAB APCs. The assault force was led by Lecointre, who approached the northern edge of the 
bridge following the usual route of the UN convoys. Fourteen VRS soldiers were in the post at the time of the assault.
[13] With bayonets fixed,[14] the French marines overran a bunker held by the VRS, at the cost of the life of one 
Frenchman, Private Jacky Humblot [fr]. The assault was supported by 90-millimetre (3.5 in) direct fire from the armoured
cars, and heavy machine-gun fire. The VRS responded with mortar bombs and fire from anti-aircraft weapons. The second 
French soldier to die in the battle, Private Marcel Amaru [fr], was killed by a sniper while supporting the assault from
 Sarajevo's Jewish cemetery. Seventeen French soldiers were wounded in the clash,[15][16] while four VRS soldiers were
killed, several more were wounded, and four were taken prisoner.
ARBiH snipers joined the fight on their own initiative, accidentally shooting and wounding one French hostage. At the 
conclusion of the 32-minute-long firefight, the VRS remained in control of the southern end of the bridge, while the 
French occupied the northern end.[10] The VRS then obtained a truce to recover their dead and wounded, under the threat 
of killing the French hostages. The wounded French soldier was immediately released and evacuated to a UN hospital. 
The VRS eventually gave up and abandoned the southern end of the bridge. The second French soldier held as hostage at 
the bridge, a corporal, managed to escape. The VRS soldiers captured in the action were treated as prisoners of war and 
detained at an UNPROFOR facility.
"""
print(len(text.split()))
text = text.replace('.', '').replace(',', '')
new_dict = {item: text.count(item) for item in text.split()}
print(new_dict)
