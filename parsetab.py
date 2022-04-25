
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftNOTleftGTLTNOTEQEQUALLTEGTErightASSIGNleftMODleftSUMSUBleftMULDIVleftIFTHENleftELSEAND ASSIGN BEGIN COLON COMMA DIV DO ELSE END EQUAL FALSE FLOAT FLOAT_KW GT GTE IDENTIFIER IF INTEGER INT_KW LRB LT LTE MOD MUL NOT NOTEQ OR PROCEDURE PROGRAM RRB SEMICOLON SUB SUM THEN TRUE VAR WHILEprogram : PROGRAM IDENTIFIER declarations proclist cmp_stmtdeclarations :\n                        | VAR declistdeclist : idlist COLON typedeclist : declist COLON idlist COLON typeidlist : IDENTIFIERidlist : idlist COMMA IDENTIFIERtype : INT_KWtype : FLOAT_KWproclist : \n                    | proclist  procproc : PROCEDURE IDENTIFIER parameters COLON declarations cmp_stmtparameters : \n                      | LRB declist RRBcmp_stmt : BEGIN stmtlist ENDstmtlist : stmtstmtlist : stmtlist COLON stmtstmt : IDENTIFIER ASSIGN expstmt : IF exp THEN stmt ELSE stmtstmt : IF exp THEN stmtstmt : WHILE exp DO stmtstmt : cmp_stmtstmt : IDENTIFIER argsstmt : args : \n                | LRB act_paramlist RRBact_paramlist : act_paramlist COMMA act_paramact_paramlist : act_paramact_param : expexp : INTEGERexp : FLOATexp : IDENTIFIERexp : exp SUM exp\n               | exp SUB exp \n               | exp MUL exp\n               | exp DIV exp\n               | SUB exp\n               | exp MOD exp \n               | exp LT exp \n               | exp LTE exp\n               | exp EQUAL exp \n               | exp NOTEQ exp\n               | exp GT exp\n               | exp GTE exp \n               | exp AND exp\n               | exp OR exp\n               | NOT exp\n               | LRB exp RRB'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,10,29,],[0,-1,-15,]),'IDENTIFIER':([2,5,12,13,14,16,20,21,30,31,33,38,39,40,43,50,51,52,53,54,55,56,57,58,59,60,61,62,63,67,72,92,],[3,9,19,23,9,28,37,37,19,37,37,37,37,37,9,19,37,37,37,37,37,37,37,37,37,37,37,37,37,19,37,19,]),'BEGIN':([3,4,6,7,11,12,25,26,27,29,30,50,67,68,70,89,92,93,],[-2,-10,12,-3,-11,12,-4,-8,-9,-15,12,12,12,-2,-5,12,12,-12,]),'PROCEDURE':([3,4,6,7,11,25,26,27,29,70,93,],[-2,-10,13,-3,-11,-4,-8,-9,-15,-5,-12,]),'VAR':([3,68,],[5,5,]),'COLON':([7,8,9,12,17,18,19,22,23,24,25,26,27,28,29,30,32,35,36,37,42,45,46,50,64,65,67,69,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,92,94,],[14,15,-6,-24,30,-16,-25,-22,-13,44,-4,-8,-9,-7,-15,-24,-23,-30,-31,-32,68,-17,-18,-24,-37,-47,-24,14,-5,-26,-20,-33,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,-45,-46,-48,-21,-14,-24,-19,]),'COMMA':([8,9,24,28,35,36,37,47,48,49,64,65,74,75,76,77,78,79,80,81,82,83,84,85,86,87,91,],[16,-6,16,-7,-30,-31,-32,72,-28,-29,-37,-47,-33,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,-45,-46,-48,-27,]),'IF':([12,30,50,67,92,],[20,20,20,20,20,]),'WHILE':([12,30,50,67,92,],[21,21,21,21,21,]),'END':([12,17,18,19,22,29,30,32,35,36,37,45,46,50,64,65,67,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,92,94,],[-24,29,-16,-25,-22,-15,-24,-23,-30,-31,-32,-17,-18,-24,-37,-47,-24,-26,-20,-33,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,-45,-46,-48,-21,-24,-19,]),'INT_KW':([15,44,],[26,26,]),'FLOAT_KW':([15,44,],[27,27,]),'ASSIGN':([19,],[31,]),'ELSE':([19,22,29,32,35,36,37,46,50,64,65,67,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,92,94,],[-25,-22,-15,-23,-30,-31,-32,-18,-24,-37,-47,-24,-26,92,-33,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,-45,-46,-48,-21,-24,-19,]),'LRB':([19,20,21,23,31,33,38,39,40,51,52,53,54,55,56,57,58,59,60,61,62,63,72,],[33,40,40,43,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'INTEGER':([20,21,31,33,38,39,40,51,52,53,54,55,56,57,58,59,60,61,62,63,72,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'FLOAT':([20,21,31,33,38,39,40,51,52,53,54,55,56,57,58,59,60,61,62,63,72,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'SUB':([20,21,31,33,34,35,36,37,38,39,40,41,46,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,],[38,38,38,38,52,-30,-31,-32,38,38,38,52,52,52,38,38,38,38,38,38,38,38,38,38,38,38,38,-37,52,52,38,-33,-34,-35,-36,52,52,52,52,52,52,52,52,52,-48,]),'NOT':([20,21,31,33,38,39,40,51,52,53,54,55,56,57,58,59,60,61,62,63,72,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'RRB':([25,26,27,35,36,37,47,48,49,64,65,66,69,70,74,75,76,77,78,79,80,81,82,83,84,85,86,87,91,],[-4,-8,-9,-30,-31,-32,71,-28,-29,-37,-47,87,90,-5,-33,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,-45,-46,-48,-27,]),'THEN':([34,35,36,37,64,65,74,75,76,77,78,79,80,81,82,83,84,85,86,87,],[50,-30,-31,-32,-37,-47,-33,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,-45,-46,-48,]),'SUM':([34,35,36,37,41,46,49,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,],[51,-30,-31,-32,51,51,51,-37,51,51,-33,-34,-35,-36,51,51,51,51,51,51,51,51,51,-48,]),'MUL':([34,35,36,37,41,46,49,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,],[53,-30,-31,-32,53,53,53,53,53,53,53,53,-35,-36,53,53,53,53,53,53,53,53,53,-48,]),'DIV':([34,35,36,37,41,46,49,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,],[54,-30,-31,-32,54,54,54,54,54,54,54,54,-35,-36,54,54,54,54,54,54,54,54,54,-48,]),'MOD':([34,35,36,37,41,46,49,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,],[55,-30,-31,-32,55,55,55,-37,55,55,-33,-34,-35,-36,-38,55,55,55,55,55,55,55,55,-48,]),'LT':([34,35,36,37,41,46,49,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,],[56,-30,-31,-32,56,56,56,-37,56,56,-33,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,56,56,-48,]),'LTE':([34,35,36,37,41,46,49,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,],[57,-30,-31,-32,57,57,57,-37,57,57,-33,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,57,57,-48,]),'EQUAL':([34,35,36,37,41,46,49,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,],[58,-30,-31,-32,58,58,58,-37,58,58,-33,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,58,58,-48,]),'NOTEQ':([34,35,36,37,41,46,49,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,],[59,-30,-31,-32,59,59,59,-37,59,59,-33,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,59,59,-48,]),'GT':([34,35,36,37,41,46,49,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,],[60,-30,-31,-32,60,60,60,-37,60,60,-33,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,60,60,-48,]),'GTE':([34,35,36,37,41,46,49,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,],[61,-30,-31,-32,61,61,61,-37,61,61,-33,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,61,61,-48,]),'AND':([34,35,36,37,41,46,49,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,],[62,-30,-31,-32,62,62,62,-37,-47,62,-33,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,-45,62,-48,]),'OR':([34,35,36,37,41,46,49,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,87,],[63,-30,-31,-32,63,63,63,-37,-47,63,-33,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,-45,-46,-48,]),'DO':([35,36,37,41,64,65,74,75,76,77,78,79,80,81,82,83,84,85,86,87,],[-30,-31,-32,67,-37,-47,-33,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,-45,-46,-48,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declarations':([3,68,],[4,89,]),'proclist':([4,],[6,]),'declist':([5,43,],[7,69,]),'idlist':([5,14,43,],[8,24,8,]),'cmp_stmt':([6,12,30,50,67,89,92,],[10,22,22,22,22,93,22,]),'proc':([6,],[11,]),'stmtlist':([12,],[17,]),'stmt':([12,30,50,67,92,],[18,45,73,88,94,]),'type':([15,44,],[25,70,]),'args':([19,],[32,]),'exp':([20,21,31,33,38,39,40,51,52,53,54,55,56,57,58,59,60,61,62,63,72,],[34,41,46,49,64,65,66,74,75,76,77,78,79,80,81,82,83,84,85,86,49,]),'parameters':([23,],[42,]),'act_paramlist':([33,],[47,]),'act_param':([33,72,],[48,91,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM IDENTIFIER declarations proclist cmp_stmt','program',5,'p_program','parser.py',12),
  ('declarations -> <empty>','declarations',0,'p_declarations','parser.py',16),
  ('declarations -> VAR declist','declarations',2,'p_declarations','parser.py',17),
  ('declist -> idlist COLON type','declist',3,'p_declist_idlist','parser.py',21),
  ('declist -> declist COLON idlist COLON type','declist',5,'p_declist_declist','parser.py',25),
  ('idlist -> IDENTIFIER','idlist',1,'p_idlist_id','parser.py',29),
  ('idlist -> idlist COMMA IDENTIFIER','idlist',3,'p_idlist_idlist','parser.py',33),
  ('type -> INT_KW','type',1,'p_type_integer','parser.py',37),
  ('type -> FLOAT_KW','type',1,'p_type_float','parser.py',41),
  ('proclist -> <empty>','proclist',0,'p_proclist','parser.py',45),
  ('proclist -> proclist proc','proclist',2,'p_proclist','parser.py',46),
  ('proc -> PROCEDURE IDENTIFIER parameters COLON declarations cmp_stmt','proc',6,'p_proc','parser.py',50),
  ('parameters -> <empty>','parameters',0,'p_parameters','parser.py',54),
  ('parameters -> LRB declist RRB','parameters',3,'p_parameters','parser.py',55),
  ('cmp_stmt -> BEGIN stmtlist END','cmp_stmt',3,'p_cmp_stmt','parser.py',59),
  ('stmtlist -> stmt','stmtlist',1,'p_stmtlist_stmt','parser.py',63),
  ('stmtlist -> stmtlist COLON stmt','stmtlist',3,'p_stmtlist_stmtlist','parser.py',67),
  ('stmt -> IDENTIFIER ASSIGN exp','stmt',3,'p_stmt_id','parser.py',71),
  ('stmt -> IF exp THEN stmt ELSE stmt','stmt',6,'p_stmt_if_then_else','parser.py',75),
  ('stmt -> IF exp THEN stmt','stmt',4,'p_stmt_if_then','parser.py',79),
  ('stmt -> WHILE exp DO stmt','stmt',4,'p_stmt_while_do','parser.py',83),
  ('stmt -> cmp_stmt','stmt',1,'p_stmt_cmp_stmt','parser.py',87),
  ('stmt -> IDENTIFIER args','stmt',2,'p_stmt_id_args','parser.py',91),
  ('stmt -> <empty>','stmt',0,'p_stmt_empty','parser.py',95),
  ('args -> <empty>','args',0,'p_args','parser.py',99),
  ('args -> LRB act_paramlist RRB','args',3,'p_args','parser.py',100),
  ('act_paramlist -> act_paramlist COMMA act_param','act_paramlist',3,'p_act_paramlist_act_paramlist','parser.py',104),
  ('act_paramlist -> act_param','act_paramlist',1,'p_act_paramlist_act_param','parser.py',108),
  ('act_param -> exp','act_param',1,'p_act_param_exp','parser.py',112),
  ('exp -> INTEGER','exp',1,'p_exp_integer','parser.py',120),
  ('exp -> FLOAT','exp',1,'p_exp_float','parser.py',124),
  ('exp -> IDENTIFIER','exp',1,'p_exp_id','parser.py',128),
  ('exp -> exp SUM exp','exp',3,'p_exp_operator','parser.py',132),
  ('exp -> exp SUB exp','exp',3,'p_exp_operator','parser.py',133),
  ('exp -> exp MUL exp','exp',3,'p_exp_operator','parser.py',134),
  ('exp -> exp DIV exp','exp',3,'p_exp_operator','parser.py',135),
  ('exp -> SUB exp','exp',2,'p_exp_operator','parser.py',136),
  ('exp -> exp MOD exp','exp',3,'p_exp_operator','parser.py',137),
  ('exp -> exp LT exp','exp',3,'p_exp_operator','parser.py',138),
  ('exp -> exp LTE exp','exp',3,'p_exp_operator','parser.py',139),
  ('exp -> exp EQUAL exp','exp',3,'p_exp_operator','parser.py',140),
  ('exp -> exp NOTEQ exp','exp',3,'p_exp_operator','parser.py',141),
  ('exp -> exp GT exp','exp',3,'p_exp_operator','parser.py',142),
  ('exp -> exp GTE exp','exp',3,'p_exp_operator','parser.py',143),
  ('exp -> exp AND exp','exp',3,'p_exp_operator','parser.py',144),
  ('exp -> exp OR exp','exp',3,'p_exp_operator','parser.py',145),
  ('exp -> NOT exp','exp',2,'p_exp_operator','parser.py',146),
  ('exp -> LRB exp RRB','exp',3,'p_exp_operator','parser.py',147),
]
