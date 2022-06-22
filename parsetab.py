
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftNOTleftGTLTNOTEQEQUALLTEGTErightASSIGNleftMODleftSUMSUBleftMULDIVleftIFTHENleftELSEAND ASSIGN BEGIN COLON COMMA DIV DO ELSE END EQUAL FALSE FLOAT FLOAT_KW GT GTE IDENTIFIER IF INTEGER INT_KW LRB LT LTE MOD MUL NOT NOTEQ OR PROCEDURE PROGRAM RRB SEMICOLON SUB SUM THEN TRUE VAR WHILEprogram : PROGRAM IDENTIFIER declarations proclist cmp_stmtdeclarations : declarations : VAR declist declist : idlist COLON type SEMICOLONdeclist : declist idlist COLON type SEMICOLONidlist : IDENTIFIERidlist : idlist COMMA IDENTIFIERtype : INT_KWtype : FLOAT_KWproclist : proc proclistproclist : proc : PROCEDURE IDENTIFIER parameters COLON declarations cmp_stmtparameters : \n                      | LRB declist RRBcmp_stmt : BEGIN stmtlist ENDstmtlist : stmtstmtlist : stmtlist SEMICOLON stmtstmt : IDENTIFIER ASSIGN expstmt : IF exp THEN stmt ELSE stmtstmt : IF exp THEN stmtstmt : WHILE exp DO stmtstmt : cmp_stmtstmt : IDENTIFIER argsstmt : args : \n                | LRB act_paramlist RRBact_paramlist : act_paramlist COMMA act_paramact_paramlist : act_paramact_param : expexp : INTEGERexp : FLOATexp : IDENTIFIERexp : exp LT exp \n               | exp LTE exp\n               | exp EQUAL exp \n               | exp NOTEQ exp\n               | exp GT exp\n               | exp GTE exp \n               | exp AND exp\n               | exp OR exp\n               | NOT exp\n               | LRB exp RRB\n        exp : exp SUM exp\n            | exp SUB exp\n            | exp DIV exp\n            | exp MOD exp\n            | exp MUL exp\n        exp : SUB exp'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,12,32,],[0,-1,-15,]),'IDENTIFIER':([2,5,8,9,13,18,22,23,26,33,34,36,41,42,43,46,48,54,55,56,57,58,59,60,61,62,63,64,65,66,67,71,74,76,95,],[3,11,15,11,21,31,40,40,11,21,40,40,40,40,40,11,-4,21,40,40,40,40,40,40,40,40,40,40,40,40,40,21,-5,40,21,]),'PROCEDURE':([3,4,7,9,32,48,74,93,],[-2,8,8,-3,-15,-4,-5,-12,]),'BEGIN':([3,4,6,7,9,13,14,32,33,45,48,54,71,72,74,93,95,],[-2,-11,13,-11,-3,13,-10,-15,13,-2,-4,13,13,13,-5,-12,13,]),'VAR':([3,45,],[5,5,]),'COLON':([10,11,15,16,25,31,73,],[17,-6,-13,27,45,-7,-14,]),'COMMA':([10,11,16,31,38,39,40,51,52,53,68,70,78,79,80,81,82,83,84,85,86,87,88,89,90,91,94,],[18,-6,18,-7,-30,-31,-32,76,-28,-29,-41,-48,-33,-34,-35,-36,-37,-38,-39,-40,-43,-44,-45,-46,-47,-42,-27,]),'IF':([13,33,54,71,95,],[22,22,22,22,22,]),'WHILE':([13,33,54,71,95,],[23,23,23,23,23,]),'END':([13,19,20,21,24,32,33,35,38,39,40,49,50,54,68,70,71,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,95,96,],[-24,32,-16,-25,-22,-15,-24,-23,-30,-31,-32,-17,-18,-24,-41,-48,-24,-26,-20,-33,-34,-35,-36,-37,-38,-39,-40,-43,-44,-45,-46,-47,-42,-21,-24,-19,]),'SEMICOLON':([13,19,20,21,24,28,29,30,32,33,35,38,39,40,47,49,50,54,68,70,71,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,95,96,],[-24,33,-16,-25,-22,48,-8,-9,-15,-24,-23,-30,-31,-32,74,-17,-18,-24,-41,-48,-24,-26,-20,-33,-34,-35,-36,-37,-38,-39,-40,-43,-44,-45,-46,-47,-42,-21,-24,-19,]),'LRB':([15,21,22,23,34,36,41,42,43,55,56,57,58,59,60,61,62,63,64,65,66,67,76,],[26,36,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'INT_KW':([17,27,],[29,29,]),'FLOAT_KW':([17,27,],[30,30,]),'ASSIGN':([21,],[34,]),'ELSE':([21,24,32,35,38,39,40,50,54,68,70,71,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,95,96,],[-25,-22,-15,-23,-30,-31,-32,-18,-24,-41,-48,-24,-26,95,-33,-34,-35,-36,-37,-38,-39,-40,-43,-44,-45,-46,-47,-42,-21,-24,-19,]),'INTEGER':([22,23,34,36,41,42,43,55,56,57,58,59,60,61,62,63,64,65,66,67,76,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'FLOAT':([22,23,34,36,41,42,43,55,56,57,58,59,60,61,62,63,64,65,66,67,76,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'NOT':([22,23,34,36,41,42,43,55,56,57,58,59,60,61,62,63,64,65,66,67,76,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'SUB':([22,23,34,36,37,38,39,40,41,42,43,44,50,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,],[43,43,43,43,64,-30,-31,-32,43,43,43,64,64,64,43,43,43,43,43,43,43,43,43,43,43,43,43,64,64,-48,43,64,64,64,64,64,64,64,64,-43,-44,-45,64,-47,-42,]),'THEN':([37,38,39,40,68,70,78,79,80,81,82,83,84,85,86,87,88,89,90,91,],[54,-30,-31,-32,-41,-48,-33,-34,-35,-36,-37,-38,-39,-40,-43,-44,-45,-46,-47,-42,]),'LT':([37,38,39,40,44,50,53,68,69,70,78,79,80,81,82,83,84,85,86,87,88,89,90,91,],[55,-30,-31,-32,55,55,55,55,55,-48,-33,-34,-35,-36,-37,-38,55,55,-43,-44,-45,-46,-47,-42,]),'LTE':([37,38,39,40,44,50,53,68,69,70,78,79,80,81,82,83,84,85,86,87,88,89,90,91,],[56,-30,-31,-32,56,56,56,56,56,-48,-33,-34,-35,-36,-37,-38,56,56,-43,-44,-45,-46,-47,-42,]),'EQUAL':([37,38,39,40,44,50,53,68,69,70,78,79,80,81,82,83,84,85,86,87,88,89,90,91,],[57,-30,-31,-32,57,57,57,57,57,-48,-33,-34,-35,-36,-37,-38,57,57,-43,-44,-45,-46,-47,-42,]),'NOTEQ':([37,38,39,40,44,50,53,68,69,70,78,79,80,81,82,83,84,85,86,87,88,89,90,91,],[58,-30,-31,-32,58,58,58,58,58,-48,-33,-34,-35,-36,-37,-38,58,58,-43,-44,-45,-46,-47,-42,]),'GT':([37,38,39,40,44,50,53,68,69,70,78,79,80,81,82,83,84,85,86,87,88,89,90,91,],[59,-30,-31,-32,59,59,59,59,59,-48,-33,-34,-35,-36,-37,-38,59,59,-43,-44,-45,-46,-47,-42,]),'GTE':([37,38,39,40,44,50,53,68,69,70,78,79,80,81,82,83,84,85,86,87,88,89,90,91,],[60,-30,-31,-32,60,60,60,60,60,-48,-33,-34,-35,-36,-37,-38,60,60,-43,-44,-45,-46,-47,-42,]),'AND':([37,38,39,40,44,50,53,68,69,70,78,79,80,81,82,83,84,85,86,87,88,89,90,91,],[61,-30,-31,-32,61,61,61,-41,61,-48,-33,-34,-35,-36,-37,-38,-39,61,-43,-44,-45,-46,-47,-42,]),'OR':([37,38,39,40,44,50,53,68,69,70,78,79,80,81,82,83,84,85,86,87,88,89,90,91,],[62,-30,-31,-32,62,62,62,-41,62,-48,-33,-34,-35,-36,-37,-38,-39,-40,-43,-44,-45,-46,-47,-42,]),'SUM':([37,38,39,40,44,50,53,68,69,70,78,79,80,81,82,83,84,85,86,87,88,89,90,91,],[63,-30,-31,-32,63,63,63,63,63,-48,63,63,63,63,63,63,63,63,-43,-44,-45,63,-47,-42,]),'DIV':([37,38,39,40,44,50,53,68,69,70,78,79,80,81,82,83,84,85,86,87,88,89,90,91,],[65,-30,-31,-32,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,-45,65,-47,-42,]),'MOD':([37,38,39,40,44,50,53,68,69,70,78,79,80,81,82,83,84,85,86,87,88,89,90,91,],[66,-30,-31,-32,66,66,66,66,66,-48,66,66,66,66,66,66,66,66,-43,-44,-45,-46,-47,-42,]),'MUL':([37,38,39,40,44,50,53,68,69,70,78,79,80,81,82,83,84,85,86,87,88,89,90,91,],[67,-30,-31,-32,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,-45,67,-47,-42,]),'DO':([38,39,40,44,68,70,78,79,80,81,82,83,84,85,86,87,88,89,90,91,],[-30,-31,-32,71,-41,-48,-33,-34,-35,-36,-37,-38,-39,-40,-43,-44,-45,-46,-47,-42,]),'RRB':([38,39,40,46,48,51,52,53,68,69,70,74,78,79,80,81,82,83,84,85,86,87,88,89,90,91,94,],[-30,-31,-32,73,-4,75,-28,-29,-41,91,-48,-5,-33,-34,-35,-36,-37,-38,-39,-40,-43,-44,-45,-46,-47,-42,-27,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declarations':([3,45,],[4,72,]),'proclist':([4,7,],[6,14,]),'proc':([4,7,],[7,7,]),'declist':([5,26,],[9,46,]),'idlist':([5,9,26,46,],[10,16,10,16,]),'cmp_stmt':([6,13,33,54,71,72,95,],[12,24,24,24,24,93,24,]),'stmtlist':([13,],[19,]),'stmt':([13,33,54,71,95,],[20,49,77,92,96,]),'parameters':([15,],[25,]),'type':([17,27,],[28,47,]),'args':([21,],[35,]),'exp':([22,23,34,36,41,42,43,55,56,57,58,59,60,61,62,63,64,65,66,67,76,],[37,44,50,53,68,69,70,78,79,80,81,82,83,84,85,86,87,88,89,90,53,]),'act_paramlist':([36,],[51,]),'act_param':([36,76,],[52,94,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM IDENTIFIER declarations proclist cmp_stmt','program',5,'p_program','parser.py',12),
  ('declarations -> <empty>','declarations',0,'p_dec_empty','parser.py',16),
  ('declarations -> VAR declist','declarations',2,'p_dec_declist','parser.py',21),
  ('declist -> idlist COLON type SEMICOLON','declist',4,'p_declist_idlist','parser.py',26),
  ('declist -> declist idlist COLON type SEMICOLON','declist',5,'p_declist_declist','parser.py',31),
  ('idlist -> IDENTIFIER','idlist',1,'p_idlist_id','parser.py',36),
  ('idlist -> idlist COMMA IDENTIFIER','idlist',3,'p_idlist_idlist','parser.py',41),
  ('type -> INT_KW','type',1,'p_type_integer','parser.py',46),
  ('type -> FLOAT_KW','type',1,'p_type_float','parser.py',51),
  ('proclist -> proc proclist','proclist',2,'p_proclist_proclist','parser.py',56),
  ('proclist -> <empty>','proclist',0,'p_proclist_empty','parser.py',61),
  ('proc -> PROCEDURE IDENTIFIER parameters COLON declarations cmp_stmt','proc',6,'p_proc','parser.py',66),
  ('parameters -> <empty>','parameters',0,'p_parameters','parser.py',71),
  ('parameters -> LRB declist RRB','parameters',3,'p_parameters','parser.py',72),
  ('cmp_stmt -> BEGIN stmtlist END','cmp_stmt',3,'p_cmp_stmt','parser.py',77),
  ('stmtlist -> stmt','stmtlist',1,'p_stmtlist_stmt','parser.py',82),
  ('stmtlist -> stmtlist SEMICOLON stmt','stmtlist',3,'p_stmtlist_stmtlist','parser.py',87),
  ('stmt -> IDENTIFIER ASSIGN exp','stmt',3,'p_stmt_id','parser.py',92),
  ('stmt -> IF exp THEN stmt ELSE stmt','stmt',6,'p_stmt_if_then_else','parser.py',97),
  ('stmt -> IF exp THEN stmt','stmt',4,'p_stmt_if_then','parser.py',102),
  ('stmt -> WHILE exp DO stmt','stmt',4,'p_stmt_while_do','parser.py',107),
  ('stmt -> cmp_stmt','stmt',1,'p_stmt_cmp_stmt','parser.py',112),
  ('stmt -> IDENTIFIER args','stmt',2,'p_stmt_id_args','parser.py',117),
  ('stmt -> <empty>','stmt',0,'p_stmt_empty','parser.py',122),
  ('args -> <empty>','args',0,'p_args','parser.py',127),
  ('args -> LRB act_paramlist RRB','args',3,'p_args','parser.py',128),
  ('act_paramlist -> act_paramlist COMMA act_param','act_paramlist',3,'p_act_paramlist_act_paramlist','parser.py',133),
  ('act_paramlist -> act_param','act_paramlist',1,'p_act_paramlist_act_param','parser.py',138),
  ('act_param -> exp','act_param',1,'p_act_param_exp','parser.py',143),
  ('exp -> INTEGER','exp',1,'p_exp_integer','parser.py',152),
  ('exp -> FLOAT','exp',1,'p_exp_float','parser.py',157),
  ('exp -> IDENTIFIER','exp',1,'p_exp_id','parser.py',162),
  ('exp -> exp LT exp','exp',3,'p_exp_operator','parser.py',167),
  ('exp -> exp LTE exp','exp',3,'p_exp_operator','parser.py',168),
  ('exp -> exp EQUAL exp','exp',3,'p_exp_operator','parser.py',169),
  ('exp -> exp NOTEQ exp','exp',3,'p_exp_operator','parser.py',170),
  ('exp -> exp GT exp','exp',3,'p_exp_operator','parser.py',171),
  ('exp -> exp GTE exp','exp',3,'p_exp_operator','parser.py',172),
  ('exp -> exp AND exp','exp',3,'p_exp_operator','parser.py',173),
  ('exp -> exp OR exp','exp',3,'p_exp_operator','parser.py',174),
  ('exp -> NOT exp','exp',2,'p_exp_operator','parser.py',175),
  ('exp -> LRB exp RRB','exp',3,'p_exp_operator','parser.py',176),
  ('exp -> exp SUM exp','exp',3,'p_exp_arithmetic','parser.py',182),
  ('exp -> exp SUB exp','exp',3,'p_exp_arithmetic','parser.py',183),
  ('exp -> exp DIV exp','exp',3,'p_exp_arithmetic','parser.py',184),
  ('exp -> exp MOD exp','exp',3,'p_exp_arithmetic','parser.py',185),
  ('exp -> exp MUL exp','exp',3,'p_exp_arithmetic','parser.py',186),
  ('exp -> SUB exp','exp',2,'p_exp_sub','parser.py',192),
]
