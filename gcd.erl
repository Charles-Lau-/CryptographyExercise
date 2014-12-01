-module(gcd).
-export([		gcd/2]).



gcd(X,Y) when X>Y->
	case X rem Y of 
		0 ->
			Y;
		Rest ->
		  gcd(Y,Rest)
	end;

gcd(X,Y) ->
	gcd(Y,X).