package com.codingdojo.LoginRegistration.service;

import java.util.List;
import java.util.Optional;

import org.mindrot.jbcrypt.BCrypt;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.validation.BindingResult;

import com.codingdojo.LoginRegistration.model.LoginUser;
import com.codingdojo.LoginRegistration.model.User;
import com.codingdojo.LoginRegistration.repo.UserRepo;

@Service
public class UserService {
	@Autowired
	private UserRepo userRepo;
	
	public User register(User newUser, BindingResult result) {
// TO-DO - Reject values or register if no errors:
		// Reject if email is taken (present in database)
		// Reject if password doesn't match confirmation
		Optional<User> potentialUser = userRepo.findByEmail(newUser.getEmail());

		if(!newUser.getPassword().equals(newUser.getConfirm())) {
			result.rejectValue("confirm", "Matches", "The Confirm Password must match Password!");
		}
		if (potentialUser.isPresent()) {
			result.rejectValue("email", "Matches", "An account with that email already exists!");	
		}
		if (result.hasErrors()) {
			return null;
		}

		String hashedString= BCrypt.hashpw(newUser.getPassword(), BCrypt.gensalt());
        newUser.setPassword(hashedString);
        return userRepo.save(newUser);

	}
	public User login(LoginUser newLoginUser, BindingResult result) {
// TO-DO - Reject values:
        Optional<User> potentialUser= userRepo.findByEmail(newLoginUser.getEmailString());
    	if (!potentialUser.isPresent()) {
			result.rejectValue("emailString", "Matches", "User not found");
			return null;
    	}
    	User user= potentialUser.get();
    	if(!BCrypt.checkpw(newLoginUser.getPasswordString(), user.getPassword())) {
    		result.rejectValue("passwordString", "Matches", "Invalid Password!");
    	}
    	if (result.hasErrors()) {
			return null;
		}
		return user;
	}
	public User findById(Long id) {
		Optional<User> potentialUser= userRepo.findById(id);
		if(potentialUser.isPresent()) {
			return potentialUser.get();
		}
		return null;
	}
	public List<User> allUsers(){
		return userRepo.findAll();
	}
	
	public User updateUser(User user) {
		return userRepo.save(user);
	}
	
}
