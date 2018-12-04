import sys
from copy import deepcopy

def main():
	global truth_assign;

	N_input = 5; #The number of literals in the SAT problem 
	N_clauses = 4; #The number of clauses in the SAT problem

	#S1=[[1,-1],[2,3],[-2,3],[2,3],[-2,-4],[2,4],[4,-2]]; #SAT
	#S1 = [[1,-2,-3,2],[-2,3],[-1,-2],[-3],[-3]]; # The set of clauses in the SAT problem #SAT
	#S1 = [[1,2],[2,-1],[1,-3],[-1,-3],[1,3],[3,-1]]; #UNSAT
	#S1 = [[-1,2,-3],[-1,3],[1,-3]]; #SAT
	S1 = [[1,2,-3],[-2,-4],[-4,-5],[-1,-5],[-3,5]]; #SAT
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

	#literals=[2,3,4]

	print("CNF: ",S_taut)
	print("Literals: ",literals)

	path=[];
	path.append(literals[0]);
	count_2 = 0;

	while True:
		count_2+=1;
		print(count_2)
		#print("CNF1:",S_taut)
		CNF = deepcopy(S_taut);
		#print("CNF2:",CNF)
		UNSAT_total = 0;
		deleted_lit=[];
		UNSAT = 0;
		SAT = 0;
		print("PATH: ",path);
		print("CNF:",CNF)
		for unit_clause in path:
			if [-1*unit_clause] in CNF:
				UNSAT =1;
				break;

			if unit_clause>0:
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
			elif unit_clause<0:
				count_1=0;
				for j in CNF:
					if unit_clause in j:
						deleted_lit.append(count_1);
					elif -1*unit_clause in j:
						if -1*unit_clause==j[0] and len(j)==1:
							deleted_lit.append(count_1);
						else:
							j.remove(-1*unit_clause);
					count_1+=1;

				for index in sorted(deleted_lit,reverse=True):
					del CNF[index];
			deleted_lit=[];

			for j in CNF:
				if len(j) == 1:
					for i in CNF:
						if -1*j[0] == i[0] and len(i)==1 and len(j)==1:
							UNSAT = 1;
							break;

			if UNSAT == 1:
				break;



		print("CNF:",CNF)
		for j in CNF:
			if len(j) == 1:
				for i in CNF:
					if -1*j[0] == i[0] and len(i)==1 and len(j)==1:
						UNSAT = 1;

		print("UNSAT: ", UNSAT);
		print("SAT: ",SAT);

		CNF_11 = []
		for i in CNF:
			if i not in CNF_11:
				i = list(set(i))
				CNF_11.append(i)

		if CNF_11 == [] and UNSAT != 1:
			SAT = 1;
			print("SATISFIABLE!")
			print("The Final Path is : ", path);
			break;
		elif len(CNF_11)==1 and UNSAT != 1 and len(CNF_11[0])==1:
			SAT = 1;
			path.append(CNF_11[0][0]);
			print("SATISFIABLE!")
			print("The Final Path is : ", path);
			break;

		last = path[len(path)-1];
		if UNSAT == 1 and last>0:
			path.remove(last);
			path.append(-1*last);

		elif UNSAT == 1 and last<0:
			while last<0:
				path.remove(last);
				if len(path)==0 and last<0:
					print("UNSATISFIABLE!")
					UNSAT_total=1;
					break
				last = path[len(path)-1];
				
			if last>0:
				path.remove(last);
				path.append(-1*last);
			

			if UNSAT_total == 1:
				break;

		elif UNSAT != 1 and len(path)<N_input:
			path.append(abs(last)+1);
		# elif UNSAT != 1 and len(path)=N_input:
		# 	if last > 0:
		# 		path.remove(last);
		# 		path.append();

		# if(count_2>40):
		# 	print("Talking too long!")
		# 	break;


if __name__ == '__main__':
    main()
