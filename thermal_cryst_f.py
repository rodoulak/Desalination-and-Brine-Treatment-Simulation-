import math
import density_calc
import constants
import scaleup
#%%

class thermal_calc:
    """
    This class calculates the mass and energy balance for thermal crystallization.

    Attributes
    ----------
        T_op : float 
            Operating temperature (oC)
        Qf : float
            Inlet flow rate (kg/hr)
        Cf_s : float
        Total ion concentration of solution (g/L)
        Cf_caso4 : float
            Concentration of CaSO4 in the solution (g/L)
        T_in : float
            Inlet feed temperature (oC)
        d_sol : float
            Inlet feed density (kg/L) 
        Cf_in : float
            List of concentration of ions in the solution (g/L)
        nacl_sat_wt : float
            Weight percent of NaCl at saturation
        nacl_sol : float
            NaCl in the solution (kg/h)
        salt_solids : float
            Salt solids (kg/h)
        caso4_sol : float
            CaSO4 in the solution (kg/h)
        solid_mass : float
            Solid mass (kg/h)
        ev_mass : float
            Evaporated mass (kg/h)
        BPE : float
            Boiling point elevation (oC)
        heat_req : float
            Heat required (kJ/h)
        T_s : float
            Steam temperature (oC)
        steam_mass : float
            Steam mass (kg/h)
        cw_mass : float
            Cooling water mass (kg/h)
    """
    def __init__(self, T_op, Qf, Cf_s, Cf_caso4, T_in, Cf_in):
        self.T_op = T_op 
        self.Qf = Qf 
        self.Cf_s = Cf_s 
        self.Cf_caso4 = Cf_caso4
        self.T_in = T_in
        self.Cf_in = Cf_in
        self.nacl_sat_wt = salt_mois
        
    def mass_bal_cryst(self):
        """
        This method calculates the mass balance for thermal crystallization.
        """
        self.nacl_sat_wt = salt_mois #wt%
        self.nacl_sol = self.Qf*self.Cf_in[0]/d_sol/1000*MW_NaCl/MW_Na
        self.salt_solids = self.Qf*self.Cf_s/d_sol/1000 #kg/h
        self.caso4_sol = self.Qf*self.Cf_caso4/100 #kg/h
        self.solid_mass = (self.salt_solids)/(1-salt_mois/100) #kg/h
        self.ev_mass = self.Qf-self.solid_mass #kg/h

    def heat_bal_cryst(self):
        """
        This method calculates the heat balance for thermal crystallization.
        """
        self.BPE = 0.0127*(self.nacl_sat_wt/10)**2+0.1743*(self.nacl_sat_wt/10+0.3443)*5/9 #oC
        self.heat_req = LHV_v*self.ev_mass+self.Qf*Cp_f*(T_op-self.T_in) #kJ/h
        self.T_s = self.heat_req/UA+self.T_op #steam temperature oC
        self.steam_mass = self.heat_req/LHV_s 
        self.cw_mass = (self.ev_mass*LHV_v)/(CP_cw*(T_cw_o-T_cw_f)) 


# This class calculates the concentration of different ions in the solution
class conc_cal:
    """
    A class used to calculate the concentration of different ions in a solution.

    Attributes
    ----------
    Qf : float
        Flow rate (units: m^3/h)
    solid_mass : float
        Mass of solid (units: kg)
    Cc1, Cc2, Cc3, Cc4, Cc5, Cc6 : float
        Concentrations of six different ions (units: ppm)
    d_sol : float
        Density of the solution at 40°C (units: kg/m^3)

    Methods
    -------
    molarity():
        Calculates the molarity of different ions in the solution (units: mol/L)
    conc_salt_comp():
        Calculates the concentration of different salts in the solution (units: ppm)
    salt_conc():
        Calculates the concentration of different salts in the outlet stream (units: ppm)
    """
    def __init__(self, Qf, solid_mass, C1, Cc1, C2, Cc2, C3, Cc3, C4, Cc4, C5, Cc5, C6, Cc6):
        self.Qf=Qf
        self.solid_mass=solid_mass
        self.C1=C1
        self.C2=C2
        self.C3=C3
        self.C4=C4
        self.C5=C5
        self.C6=C6
        self.cf_in=Cc1+Cc2+ Cc3+ Cc4+ Cc5+ Cc6
        self.Cc1=Cc1
        self.Cc2=Cc2
        self.Cc3=Cc3
        self.Cc4=Cc4
        self.Cc5=Cc5
        self.Cc6=Cc6
        # Calculate the density of the feed solution at T_in 
        self.d_sol=density_calc.density_calc(T_in, self.cf_in) 
    
    
    def molarity(self):        
        """This method calculates the molarity of different ions in the solution"""
        self.Cc1_mol=self.Cc1/MW_Na
        self.Cc2_mol=self.Cc2/MW_cl
        self.Cc3_mol=self.Cc3/MW_K
        self.Cc4_mol=self.Cc4/MW_Mg
        self.Cc5_mol=self.Cc5/MW_Ca
        self.Cc6_mol=self.Cc6/MW_so4
        self.CNacl_mol=self.Cc2_mol-self.Cc3_mol
        self.CKCl_mol=self.Cc3_mol
        self.CMgoh_mol=self.Cc4_mol
        self.CCaso4_mol=self.Cc6_mol
        self.CCaoh_mol=self.Cc6_mol-self.Cc5_mol
    
    def conc_salt_comp(self):
        """This method calculates the concentration of different salts in the solution"""
        self.CNacl=self.CNacl_mol*MW_NaCl
        self.CKCl=self.CKCl_mol*MW_KCl
        self.CMgoh=self.CMgoh_mol*MW_MgOH
        self.CCaso4=self.CCaso4_mol*MW_Caso4
        
    def salt_conc(self):
        """This method calculates the concentration of different salts in the outlet stream"""
        self.CNacl_out=self.CNacl*self.Qf/self.d_sol/(self.solid_mass) 
        self.CKCl_out=self.CKCl*self.Qf/self.d_sol/(self.solid_mass/d_salt)
        self.CMgoh_out=self.CMgoh*self.Qf/self.d_sol/(self.solid_mass/d_salt)
        self.CCaso4_out=self.CCaso4*self.Qf/self.d_sol/(self.solid_mass/d_salt)
        self.CNa=self.CNacl_out/MW_NaCl*MW_Na
        self.CCl=self.CNacl_out/MW_NaCl*MW_cl+self.CKCl_out/MW_KCl*MW_cl
        self.CK=self.CKCl_out/MW_KCl*MW_K
        self.CCa=self.CCaso4/MW_Caso4*MW_Ca
        self.CSO4=self.CCaso4/MW_Caso4*MW_so4
        self.CMg=self.Cc4*self.Qf/self.d_sol/(self.solid_mass/d_salt) 


def calculate_energy(Qf, Q_evap_mass, Qcw, d_sol, npump):
    """
    Calculate the energy required for thermal crystallization.

    Arguments 
    ----------
        Qf : float
            Flow rate of the feed solution in m3/h.
        Q_evap_mass : float
            Distillate flow rate m3/h.
        Qcw : float
            Flow rate of cooling water in m3/h.
        d_sol : float
            Density of the feed solution in kg/m3.
        npump : float
            Pump efficiency.

    Returns:
        tuple: A tuple containing the following:
            SEC_el : float
                Specific energy consumption for electrical energy in kWh/m3.
            SEC_el_prod : float
                Specific energy consumption for electrical energy per unit mass of evaporated water in kWh/kg.
            SEC_el_prod2 : float
                Specific energy consumption for electrical energy per unit mass of NaCl produced in kWh/kg.
    """
    
    # Calculate electrical energy consumption
    E_el_th_Cr = ((Qf*dp_f + Q_evap_mass*dp_w + M_Nacl*dp_slurry + 2*Qcw*dp_cw)*1e5/3600/(1000*npump))/1000 #kwh
    
    # Calculate thermal energy consumption
    E_th_th_Cr = th_cryst_dat.heat_req/3600 #kwh
    
    # Calculate energy consumption for filtration
    E_fil = 0#scaleup.scaleup(2.4, 4800, Qf)
    
    # Add filtration energy consumption to electrical energy consumption
    E_el_th_Cr = E_el_th_Cr + E_fil
    
    # Calculate specific electrical energy consumption per unit mass of feed 
    SEC_el_f = (E_fil + E_el_th_Cr)/(Qf*d_sol*1000)
    
    # Calculate specific electrical energy consumption per unit mass of evaporated water
    SEC_el_w = (E_fil + E_el_th_Cr)/(Q_evap_mass/1000)
    
    # Calculate specific electrical energy consumption per unit mass of NaCl produced
    SEC_el_NaCl = (E_fil + E_el_th_Cr)/(M_Nacl)
    
    return E_el_th_Cr, E_th_th_Cr, SEC_el_f, SEC_el_NaCl, SEC_el_w

def mass_balance(Qf, Cf_in, M_Nacl, Csalt_out, d_sol):
    """Calculate the mass balance."""
    for i in range(len(Cf_in)):
        bal_i = Cf_in[i]*Qf/d_sol - (M_Nacl/d_salt*Csalt_out[i])
        print(f"For {i}, mass balance equals: {bal_i}")

 #%%
#Example usage       
#constants
R=8.31446261815324 #gas constant
d_salt=1.974463 #density_salt (NaCl)=1974.5 kg/m3
    #Molecular weight 
MW_Na=constants.MW_Na
MW_cl=constants.MW_cl
MW_so4=constants.MW_so4
MW_K=constants.MW_K
MW_Ca=constants.MW_Ca
MW_Mg=constants.MW_Mg
MW_HCO3=constants.MW_HCO3
MW_NaCl=constants.MW_NaCl
MW_KCl=MW_K+MW_cl
MW_Mgso4=MW_Mg+MW_so4
MW_Caso4=MW_Ca+MW_so4
MW_Na2so4=2*MW_Na+MW_so4
MW_MgOH=constants.MW_MgOH

    # Thermodynamics 
Cp_f=3.14 # Feed specific heat capacity (units: KJ* Kg*oC)
CP_cw=4.187 # Water specific heat capacity (units: KJ* Kg*oC)
UA=45990
LHV_v=2107.92 # kj/kg (gathered from steam table)
LHV_s=2357.69 # kj/kg (gathered from steam table)

#Assumptions
dp=0.1 # pressure drop (units: bar)
dp_slurry=3.5 #pressure drop for slurry streams (units: bar)
dp_f=3.5 #pressure drop for feed (units: bar)
dp_w=1 #pressure drop for qater streams (units: bar)
dp_cw=2 #pressure drop for cooling water (units: bar) 
salt_mois=20 # % moinsture in salt stream (units: %)
npump=0.8 #pump efficiency (units: -)


#Input parameters
T_in=40 #oC
T_top=60 #oC
T_cw_f=25 #oC
T_cw_o=40 #oC
T_op=60 #oC

#Feed flowrate
Qf=1000 #kg/h

#Feed concentration 
Cf_in=[80.42, 116.69, 2.29, 0.01, 0.04, 0.54] #[Na, Cl, K, Mg, Ca, SO4 ]
Cf_s=sum(Cf_in) #total salt concentration (g/L)
d_sol=density_calc.density_calc(T_in, Cf_s)/1000 #density of feed
Cf_caso4=Cf_in[4]*MW_Caso4/MW_Ca #CaSO4 concentration in feed solution (g/L)

#Calculation 
th_cryst_dat=thermal_calc(T_op, Qf, Cf_s, Cf_caso4, T_in, Cf_in)
th_cryst_dat.mass_bal_cryst()
th_cryst_dat.heat_bal_cryst()

#Recovered salt flow rate (kg/h)
M_Nacl=th_cryst_dat.solid_mass

# Calculation of the concentration of different ions in the solution
th_cryst_dat_2=conc_cal(Qf, M_Nacl , 'Na',Cf_in[0], 'cl',Cf_in[1],'k', Cf_in[2], 'mg', Cf_in[3], 'ca', Cf_in[4], 'so4', Cf_in[5])
th_cryst_dat_2.molarity()
th_cryst_dat_2.conc_salt_comp()
th_cryst_dat_2.salt_conc()

#Cooling water requirements (kg/h)
Qcw=th_cryst_dat.cw_mass

#Evaporation mass flow rate (water recovery), (kg/h)
Q_evap_mass=th_cryst_dat.ev_mass

#Salt stream concentration (g/L)
Csalt_out=[th_cryst_dat_2.CNa,th_cryst_dat_2.CCl, th_cryst_dat_2.CK, th_cryst_dat_2.CMg, th_cryst_dat_2.CCa, th_cryst_dat_2.CSO4]

#Mass balance 
for i in range(len(Cf_in)):
    bal_i=Cf_in[i]*Qf/d_sol-(M_Nacl/d_salt*Csalt_out[i])

#Calculate energy consumption 
E_el_th_Cr, E_th_th_Cr, SEC_el_f, SEC_el_NaCl, SEC_el_w = calculate_energy(Qf, Q_evap_mass, Qcw, d_sol, npump)
print(f"SEC_el_prod is {SEC_el_w} KWh/m3 product")
print(f"SEC_el_prod2 is {SEC_el_NaCl} KWh/kg product")
