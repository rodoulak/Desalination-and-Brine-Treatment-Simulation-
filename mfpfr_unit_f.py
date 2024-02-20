import math
import density_calc
import scaleup
from density_calc import density_calc
import math
import constants
#%%
class inputpar:
    """
    A class used to represent Mass Balance for percipitation step with the addition of alkaline solution 

    Attributes
    ----------
    MW : float
        Molecular weight of the solute (g/mol)
    Ci_in : float
        Initial concentration of the solute (g/L)
    conv_1: float
        Conversion rate for Magnisium percipitation in the first step 
    conv_2: float
        Conversion rate for Calcium percipitation in the second step    
    C_NaOH_1: float
        Concentration of NaOH solution for first step (mol/L)
    Qin
    QMg_in 
    QNaOH_1 : float 
        Volumetric flow rate of sodium hydroxide in step 1 in L/h
    M_MgOH2_1: float 
        Outlet mass flow rate of magnesium hydroxide produced in kg/h
    Qtot_out_1 : float 
        Outlet volumetric flow rate in L/h
    Mtot_out_1 : float 
        Step 1 outlet mass flow rate in kg/h
    magma_d_1 : float 
        magma density: the quantity of solids produced per volume of slurry kg/l
    ph_1 : float 
        ph of solution during first step 
    kps_MgOH : float 
        Product solubility of Mg(OH)2 
    Ci_out_1 : float 
        The outlet ion concentration from step 1 in mol/L
    QNaOH_2_st : float 
        The stoichiometric volumetric flow rate of sodium hydroxide for the second step L/hr
    QNaOH_2_add : float
        The added volumetric flow rate of sodium hydroxide needed to reach a pH = 13  L/h
    M_CaOH2_2: float 
        The outlet mass flow rate of calcium hydroxide produced during the 2nd step kg/hr 
    M_MgOH2_2 : float 
        The outlet mass flow rate of magnesium hydroxide produced during the 2nd step kg/hr 
    magma_d_2 : float    
        Magma density: the quantity of solids produced per volume of slurry kg/l
    Qtot_out_2 : float 
        Total outlet volumetric flow rate for 2nd step in L/h
    Ci_out_2 : float 
        The outlet ion concentration from step 2 in mol/L
      
    Methods
    -------
    calc_step1():
        Calculates the flowrates, the concentration of the streams and the requirements of alkaline solution in the 1st step 
    calc_step2():
        Calculates the flowrates, the concentration of the streams and the requirements of alkaline solution in the 2nd step 
        """
    def __init__(self, Qin, Cc1, Cc2, Cc3, Cc4, Cc5, Cc6, Cc7, C_NaOH_1, C_NaOH_2, conv_1, conv_2):
        self.Qin=Qin
        self.CNa_in=Cc1/MW_Na #Na concentration (g/l) to (mol/l)
        self.CCl_in=Cc2/MW_Cl #Cl concentration (g/l) to (mol/l)
        self.CK_in=Cc3/MW_K #K concentration (g/l) to (mol/l)
        self.CMg_in=Cc4/MW_Mg #Mg concentration (g/l) to (mol/l)
        self.CCa_in=Cc5/MW_Ca #Ca concentration (g/l) to (mol/l)
        self.CSO4_in=Cc6/MW_SO4 #SO4 concentration (g/l) to (mol/l)
        self.CHCO3_in=Cc7/MW_HCO3 #HCO3 concentration (g/l) to (mol/l)
        self.C_NaOH_1=C_NaOH_1 
        self.C_NaOH_2=C_NaOH_2 
        self.conv_1=conv_1 
        self.conv_2=conv_2 
    
    def calc_step1(self):
        #Calculate the molar flow rate of magnesium in the reactor during the 1° stepin mol/h
        self.QMg_in=self.Qin*self.CMg_in 
        
        #Calculate the volumetric flow rate of sodium hydroxide in L/h
        self.QNaOH_1=(self.Qin*self.CMg_in*(self.conv_1/100)*2)/self.C_NaOH_1 
        
        #Calculate outlet mass flow rate of magnesium hydroxide produced in kg/h
        self.M_MgOH2_1=(self.Qin*self.CMg_in*(self.conv_1/100)*MW_MgOH)/1000 
        
        #Calculate outlet volumetric flow rate in L/h
        self.Qtot_out_1=self.Qin+self.QNaOH_1
        
        #Calculate outlet mass flow rate in kg/h
        self.Mtot_out_1=self.Qin*d_in+self.QNaOH_1*1.04-self.M_MgOH2_1  
        
        #Calculate magma density: the quantity of solids produced per volume of slurry kg/l
        self.magma_d_1=self.M_MgOH2_1/self.Qtot_out_1 
        
        #Calculate ph of solution during the first step 
        self.ph_1=14+math.log10(2*(kps_MgOH/4)**(1/3))
        
        #Calculate total outlet volumetric flow rate in L/h
        self.Qtot_out_1=self.Qin+self.QNaOH_1-self.M_MgOH2_1/d_mgoh_2 
        
        #Calculates the outlet ion concentration in mol/L
        self.CMg_out_1=(self.QMg_in*(1-self.conv_1/100))/self.Qtot_out_1 
        self.CNa_out_1=(self.Qin*self.CNa_in+self.QNaOH_1*self.C_NaOH_1)/self.Qtot_out_1
        self.CCl_out_1=(self.Qin*self.CCl_in)/self.Qtot_out_1
        self.CK_out_1=(self.Qin*self.CK_in)/self.Qtot_out_1
        self.CCa_out_1=(self.Qin*self.CCa_in)/self.Qtot_out_1
        self.CSO4_out_1=(self.Qin*self.CSO4_in)/self.Qtot_out_1
        self.CHCO3_out_1=(self.Qin*self.CHCO3_in)/self.Qtot_out_1
        
        return self.QMg_in, self.QNaOH_1, self.M_MgOH2_1, self.Qtot_out_1, self.Mtot_out_1, self.magma_d_1, self.ph_1, self.CMg_out_1, self.CNa_out_1, self.CCl_out_1, self.CK_out_1, self.CCa_out_1, self.CSO4_out_1, self.CHCO3_out_1
    
    def calc_step2(self):
       #Calculate the molar flow rate of calcium in the reactor during the 2nd stepin mol/h
       self.QCa_in_2=self.Qtot_out_1*self.CCa_out_1 
       
       #Calculate the stoichiometric volumetric flow rate of sodium hydroxide for the second step L/hr
       self.QNaOH_2_st=(self.Qtot_out_1*(self.CCa_out_1*(self.conv_2/100)+self.CMg_out_1*1)*2)/self.C_NaOH_2 
       
       #Calculate concentration of the hydroxide ion in mol/L for a ph=13 solution  
       self.COH_ph13=10**(-(14-13)) 
       self.COH_st=10**(-(14-self.ph_1))
       print("c stixh is "+ str(self.ph_1))
       #Calculate the added volumetric flow rate of sodium hydroxide needed to reach a pH = 13  L/h
       self.QNaOH_2_add=((0.0216-self.COH_ph13)*(self.QNaOH_2_st+self.Qtot_out_1))/(self.COH_ph13-self.C_NaOH_2)
       
       #Calculate the total outlet volumetric flow rate from 2nd step L/h
       self.Qtot_out_2=self.Qtot_out_1+self.QNaOH_2_st+self.QNaOH_2_add
      
       #Calculate the outlet mass flow rate of calcium hydroxide produced during the 2nd step kg/hr 
       self.M_CaOH2_2=(self.Qtot_out_1*self.CCa_out_1*(self.conv_2/100)*MW_CaOH)/1000 #kg/hr
      
       #Calculate the outlet mass flow rate of magnesium hydroxide produced during the 2nd step kg/hr 
       self.M_MgOH2_2=self.Qtot_out_1*self.CMg_out_1*MW_MgOH/1000 
       
       #Calculate magma density: the quantity of solids produced per volume of slurry kg/l
       self.magma_d_2=(self.M_MgOH2_2+self.M_CaOH2_2)/self.Qtot_out_2 
      
       #Calculate total outlet volumetric flow rate for 2nd step in L/h
       self.Qout_2=self.Qtot_out_2-self.M_CaOH2_2/d_caoh_2-self.M_MgOH2_2/d_mgoh_2
      
       
       #Calculates the outlet ion concentration in mol/L
       self.CNa_out_2=(self.Qtot_out_1*self.CNa_out_1+(self.QNaOH_2_st+self.QNaOH_2_add)*self.C_NaOH_2)/self.Qtot_out_2       
       self.CCa_out_2=(self.QCa_in_2*(1-self.conv_2/100))/self.Qtot_out_2
       self.CCl_out_2=(self.Qtot_out_1*self.CCl_out_1)/self.Qtot_out_2
       self.CK_out_2=(self.Qtot_out_1*self.CK_out_1)/self.Qtot_out_2
       self.CMg_out_2=0
       self.CSO4_out_2=(self.Qtot_out_1*self.CSO4_out_1)/self.Qtot_out_2
       self.CHCO3_out_2=(self.Qtot_out_1*self.CHCO3_out_1)/self.Qtot_out_2
       
       #Calculate ph of solution during the second step 
       self.ph_2=14+math.log10(0.1)
    
       return self.QCa_in_2, self.QNaOH_2_st, self.COH_ph13, self.QNaOH_2_add, self.Qtot_out_2, self.M_CaOH2_2, self.M_MgOH2_2, self.magma_d_2, self.Qout_2, self.CNa_out_2, self.CCa_out_2, self.CCl_out_2, self.CK_out_2, self.CMg_out_2, self.CSO4_out_2, self.CHCO3_out_2, self.ph_2

class HClAddition:
    def __init__(self, Qout_2, Cout_all_m, MW_cl, ph_2):
        self.Qout_2 = Qout_2
        self.Cout_all_m = Cout_all_m
        self.MW_cl = MW_cl
        self.ph_2 = ph_2

    def calculate_HCl_addition(self):
        OH_initial = math.pow(10, -14) / math.pow(10, -self.ph_2)
        OH_final = math.pow(10, -14) / math.pow(10, -7)
        
        #Calculate the volume of HCl 1M in liters, Qout_f
        QHCl = (self.Qout_2 * OH_initial - self.Qout_2 * OH_final) / (OH_final + HCl_conc)  
        self.Qout_f = self.Qout_2+QHCl

        # Calculate the outlet concentration of chloride ions
        C_cl_out = (self.Cout_all_m[1] * self.Qout_2 + QHCl * HCl_conc) / self.Qout_f  # mol/l
        self.Cout_all_m[1] = C_cl_out
        C_cl_out = C_cl_out * self.MW_cl  # g/l
        Cout_mfpfr_g[1] = C_cl_out

        for i in range(2, 6):
            Cout_mfpfr_g[i] = Cout_mfpfr_g[i] * self.Qout_2 / self.Qout_f

        Cout_mfpfr_g[0] = Cout_mfpfr_g[0] * self.Qout_2 / self.Qout_f
        # Return the volume of HCl added and the outlet concentration of chloride ions
        return QHCl, Cout_mfpfr_g
     
  # Get the outlet flow rate

#%%Energy consumption 
class energycons:
    def energycalc(Qtot, QNaOH, Qin, QNaOH_1, QNaOH_2_add, QNaOH_2_st):
        Qtot=Qtot
        QNaOH=QNaOH
        Qin=Qin
        QNaOH_2_st=QNaOH_2_st
        QNaOH_2_add=QNaOH_2_add
        QNaOH_1=QNaOH_1        
        
        #Calculate the energy required for pumping in kW
        Epump_1=(Qin*dp+QNaOH_1*dp)*1e5/3600/(1000*npump) #(W)
        Epump_2=((Qin+QNaOH_1)*dp+(QNaOH_2_add+QNaOH_2_st)*dp)*1e5/3600/(1000*npump)       #(W)
        return Epump_1, Epump_2
                    
#%%
#Example usage
#Input parameters
    #molecular weight
MW_Na=constants.MW_Na
MW_Cl=constants.MW_cl
MW_SO4=constants.MW_so4
MW_K=constants.MW_K
MW_Ca=constants.MW_Ca
MW_Mg=constants.MW_Mg
MW_HCO3=constants.MW_HCO3
MW_values = [MW_Na, MW_Cl, MW_K, MW_Mg, MW_Ca, MW_SO4]
MW_MgOH=constants.MW_MgOH
MW_CaOH=constants.MW_CaOH

#constants
kps_MgOH=5.61*0.000000000001 #product solublity of Mg(OH)2
kps_CaOH=5.5*0.000001 #product solublity of Ca(OH)2
d_mgoh_2=2.34 #Mg(OH)2 density (units: kg/l)
d_caoh_2=2.211 #Ca(OH)2 density (units: kg/l)

#assumptions
dp=0.5 # pressure drop (units: bar)
dp_HCl=0.3# pressure drop HCl solution (units: bar)
npump=0.8 #pump efficiency (units: -)


# Define the input parameters
T=20+273.15 #Temperature (units: K)
C_NaOH = [1, 1]  # Concentration of NaOH solution for step 1 and step 2 in MOL/L
conv = [95, 93]  # Conversion rate for step 1 and step 2
Cin_mfpfr = [17.3, 38.6, 0.6, 4.3, 1.2, 9.9]  # Concentrations of [Na, Cl, K, Mg, Ca, SO4]
Qin_mfpfr = 1000  # Flow rate in l/hr

# Calculate the density of the input
d_in = density_calc(25, sum(Cin_mfpfr)) / 1000

# Create an instance of the inputpar class with the defined parameters
mfpfr_dat = inputpar(Qin_mfpfr, *Cin_mfpfr, 0, *C_NaOH, *conv)

# Call the calc_step1 and calc_step2 methods to calculate the necessary values
mfpfr_dat.calc_step1()
mfpfr_dat.calc_step2()
ph_2=mfpfr_dat.ph_2

# Calculate the total outlet concentration and the concentration of sulfate ions
Cour_mfpfr = sum([mfpfr_dat.CNa_out_2, mfpfr_dat.CCa_out_2, mfpfr_dat.CCl_out_2, mfpfr_dat.CK_out_2, mfpfr_dat.CMg_out_2, mfpfr_dat.CSO4_out_2]) # mol/l
CSO4_out_2 = mfpfr_dat.CSO4_out_2 # mol/l

# Calculate the concentration of sodium chloride ions
CNa_out_2 = mfpfr_dat.CNa_out_2
Cnacl_out = CNa_out_2 - 2 * CSO4_out_2

# Get the molar masses of the compounds
M_MgOH2_1 = mfpfr_dat.M_MgOH2_1
M_CaOH2 = mfpfr_dat.M_CaOH2_2
M_MgOH2 = mfpfr_dat.M_MgOH2_2

# Create a list of the outlet concentrations in mol/l
Cout_all_m = [mfpfr_dat.CNa_out_2, mfpfr_dat.CCl_out_2, mfpfr_dat.CK_out_2, mfpfr_dat.CMg_out_2, mfpfr_dat.CCa_out_2, mfpfr_dat.CSO4_out_2]

# Calculate the outlet concentrations in g/l
MW = [MW_Na, MW_Ca, MW_Cl, MW_K, MW_Mg, MW_SO4]
Cout_mfpfr_g = [Cout_all_m[i] * MW[i] for i in range(len(Cout_all_m))] # g/l

#Outlet flow rate 
Qout_2 = mfpfr_dat.Qout_2

# Calculate the chemical consumption of NaOH
QNAOH = mfpfr_dat.QNaOH_1 + mfpfr_dat.QNaOH_2_add + mfpfr_dat.QNaOH_2_st # convert to kg

#hcl to decrease ph to 7
HCl_conc=1 #l of HCl 1M
unit = HClAddition(Qout_2, Cout_all_m, MW_Cl, ph_2)

# Call the calculate_HCl_addition method
QHCl, Cout_mfpfr_g = unit.calculate_HCl_addition()


# Print the volume of HCl added and the outlet concentration of chloride ions
print(f"HCl flow rate is {QHCl} l/h")
print(f"C_out in g is {Cout_mfpfr_g} g/l")

#Calculate final outlet flow rate
Qout_f=Qout_2+QHCl #l/h
d_out_s=density_calc(25,sum(Cout_mfpfr_g))/1000 #kg/m3
Mout_2=Qout_f*d_out_s #kg/h

#electicity consumption
# Create an instance of the inputpar class with the defined parameters
Epump_1, Epump_2=energycons.energycalc(mfpfr_dat.Qout_2, QNAOH, Qin_mfpfr, mfpfr_dat.QNaOH_1, mfpfr_dat.QNaOH_2_add, mfpfr_dat.QNaOH_2_st)

#Electricity consumption for pumping , KWh
E_el_mfpf=(Epump_1+Epump_2+(QHCl*dp_HCl)*1e5/3600/(1000*npump))/1000
print("Electricity energy consumption is "+str(E_el_mfpf)+ " kw")

#Electricity consumption for filtration unit 
E_fil=scaleup.scaleup(0.5, 0.3*1000, Mout_2)

#Total electricity consumption, KWh
E_el_mfpf=E_el_mfpf+E_fil

#Specific energy consumption per kg of Mg(OH)2, KWh/kg of Mg(OH)2
SEC_el_prod=(E_el_mfpf)/(M_MgOH2)
print("SEC_el_prod is "+str(SEC_el_prod)+" KWh/kg product ")

#Specific energy consumption per feed, KWh/m3 of feed
SEC_el_feed=(E_el_mfpf)/(Qin_mfpfr/1000)
print("SEC_el_feed is "+str(SEC_el_feed)+" KWh/m3 of feed ")
