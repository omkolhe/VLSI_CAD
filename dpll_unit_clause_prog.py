import sys
from copy import deepcopy

truth_assign=[];
unit_prop = 0;
N_spilt = -1;

def dpll(CNF,lits):
	global truth_assign,unit_prop,N_spilt;

	N_spilt += 1;

	#Let the unit propagation start ------------------------------------------------------
	while True:
		if len(lits)==1 and len(CNF)>1:
			print("----------------------------------------------")
			print(CNF)
			print(lits)
			break

		deleted_lit=[];
		unit_clause = None;
		#CNF = list(set(CNF)
		print("----------------------------------------------")
		print("CNF: ",CNF)
		print("Literals: ",lits)

		#Finding if there is a unit clause in CNF 
		for i in CNF: # check unit clause
			if len(i)==1:
				unit_clause = i[0];
				truth_assign.append(unit_clause);
				print("Unit Clause: ", unit_clause);
				CNF.remove(i);
				break;

		#Finding if !(unit_clause) exist in the rest of the CNF 
		if unit_clause:
			for i in CNF:
				if -1*unit_clause == i[0] and len(i)==1:
					return False

		#Substituition the value of the unit_clause in the rest of the CNF 
		if unit_clause  and unit_clause>0:
			unit_prop+=1;
			count=0;
			for j in CNF:
				if -1*unit_clause in j:
					if -1*unit_clause == j[0] and len(j)==1:
						deleted_lit.append(count);
					else:
						j.remove(-1*unit_clause);
				elif unit_clause in j:
					deleted_lit.append(count);
				count+=1;

			for index in sorted(deleted_lit,reverse=True):
				del CNF[index];
			lits.remove(unit_clause);

		elif unit_clause  and unit_clause<0:
			unit_prop+=1;
			count_1=0;
			for j in CNF:
				if unit_clause in j:
					deleted_lit.append(count_1);
				elif -1*unit_clause in j:
					if -1*unit_clause==j[0] and len(j)==1:
						deleted_lit.append(count_1);
					else:
						j.remove(-1*unit_clause);

			for index in sorted(deleted_lit,reverse=True):
				del CNF[index];
			lits.remove(-1*unit_clause);

		else:
			break;

	#________________Unit propagation ends__________________

	#Checking termination condition 
	if CNF == []:
		return True;
	elif len(lits)==1 and len(CNF)>1:
		return False;

	#Splitting into two branches in the DPLL there
	CNF_1=[];
	CNF_2=[];
	CNF_1 = CNF.copy();
	CNF_2 = CNF.copy();
	CNF_1.append([lits[0]]);
	CNF_2.append([-1*lits[0]]);

	if dpll(CNF_1,deepcopy(lits)) or dpll(CNF_2,deepcopy(lits)):
		return True
	else:
		return False


def main():
	global truth_assign;

	N_input = 4; #The number of literals in the SAT problem 
	N_clauses = 4; #The number of clauses in the SAT problem

	S1=[[1,-1],[2,3],[-2,3],[2,3],[-2,-4],[2,4],[4,-2]];
	#S1 = [[1,-2,-3,2],[-2,3],[-1,-2],[-3],[-3]]; # The set of clauses in the SAT problem
	#S1 = [[1,2],[2,-1],[1,-3],[-1,-3],[1,3],[3,-1]];
	#S1 = [[-1,2,-3],[-1,3],[1,-3]];
	S=[]

	#Removes redundant literals in CNF
	for i in S1:
	  if i not in S:
	  	i = list(set(i))
	  	S.append(i)

	#Removing tautology
	S_taut=[]
	S_taut = S.copy()

	for i in S:
		for j in range(1,N_input+1):
			if (j in i) and (-j in i):
				S_taut.remove(i);
				continue

	#Stores all the literals present in the CNF 
	literals=[]

	for i in range(N_input):
		literals.append(i+1)

	print("CNF: ",S_taut)
	print("Literals: ",literals)
	
	#Check if the CNF is satisfiable or not 
	if dpll(S_taut,literals):
		print("---------------Result----------------")
		print("SATISFIABLE")
	else:
		print("---------------Result----------------")
		print("UNSATISFIABLE")

if __name__ == '__main__':
    main()
