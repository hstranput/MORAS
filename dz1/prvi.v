Require Import Bool.

Notation " ! b " := (negb b) (at level 0).

(* a *)
Goal forall (x y : bool), 
    ! (x && y) || (!x && y) || (!x && !y) = !x || !y.
Proof.
    now destruct x, y.
Qed.

(* b *)
Goal forall (x y z: bool), 
    !(!x && y && !z) && !(x && y && z) && (x && !y && !z) = x && !y && !z.
Proof.
    now destruct x, y, z.  
Qed.