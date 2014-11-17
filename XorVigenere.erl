-module('XorVigenere').
-export([encrypt/2,decrypt/2]).

%encrypt message with input key by using Xor Vigenere
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%format input
encrypt(Key,Message) when is_atom(Key) orelse is_atom(Message) ->
	if 
		is_atom(Key) ->
				 encrypt(atom_to_list(Key),Message);
		true ->
				 encrypt(Key,atom_to_list(Message))
	end;

encrypt(Key=[K|Rest_Key],[M|Rest_Message]) ->
	encrypt(Key,Rest_Key,Rest_Message,[K bxor M]).

%encrypt process
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%	
encrypt(_,_,[],CipherText) ->
	lists:reverse(CipherText);
	
encrypt(Key=[K|Rest_Key],[],[M|Rest_Message],CipherText) ->
	encrypt(Key,Rest_Key,Rest_Message,[K bxor M|CipherText]);
 
encrypt(Key,[K|Rest_Key],[M|Rest_Message],CipherText) ->
	encrypt(Key,Rest_Key,Rest_Message,[K bxor M|CipherText]).
	
%decrypt process just to call encrypt function again
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
decrypt(Key,CipherText) ->
	encrypt(Key,CipherText).
	 
		
	