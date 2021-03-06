package models;

import java.util.List;

import javax.persistence.Entity;
import javax.persistence.Id;

import play.data.validation.Constraints.Required;
import play.db.ebean.Model;

@Entity
public class Category extends Model{
	@Id
	public Long id;
	@Required
	public String category_name;
	public Long root_id;

	public static Finder<Long, Category> find = new Finder(Long.class, Category.class);

	public static List<Category> all(){
		return find.all();
	}

	public static Category findById(Long id){
		return find.ref(id);
	}

}




