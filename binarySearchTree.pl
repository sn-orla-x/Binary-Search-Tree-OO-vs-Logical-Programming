/*
See report for instructions on how to test
*/



node(_,_,_).


search(node(A,_,_),A) :- !.
search(node(V,L,_),A) :- A < V, search((L),A).
search(node(V,_,R),A) :- A > V, search((R),A).

insert(node(V, nil, nil),V) :- !.
insert(node(nil,nil,nil), A) :- node(A, nil, nil).
insert(nil, A) :- node(A, nil, nil).
insert(node(V, L, _), A) :- A < V, insert((L),A).
insert(node(V, _, R), A) :- A > V, insert((R),A).

inorder(nil) :- !.
inorder(node(V,nil, nil)) :- write(V), write(" "),!.
inorder(node(V,L, nil)) :- inorder(L), write(V), write(" ").
inorder(node(V, nil, R)) :- write(V), write(" "), inorder(R).
inorder(node(V, L, R)) :- inorder(L), write(V), write(" "), inorder(R).

 
preorder(nil) :- !.
preorder(node(V, nil, nil)) :- write(V), write(" "), !.
preorder(node(V, L, nil)) :- write(V), write(" "), preorder(L).
preorder(node(V, nil, R)) :- write(V), write(" "), preorder(R).
preorder(node(V,L,R)) :- write(V), write(" "), preorder(L), preorder(R).

postorder(nil) :- !.
postorder(node(V, nil, nil)) :- write(V), write(" "), !.
postorder(node(V, L, nil)) :- postorder(L), write(V), write(" ").
postorder(node(V, nil, R)) :- postorder(R), write(V), write(" ").
postorder(node(V, L, R)) :- postorder(L), postorder(R), write(V), write(" ").