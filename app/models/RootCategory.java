package models;

import java.util.List;

import javax.persistence.Entity;
import javax.persistence.Id;

import play.data.validation.Constraints.Required;
import play.db.ebean.Model;

@Entity
public class RootCategory extends Model{
	@Id
	public Long id;
	@Required
	public String name;

	public static Finder<Long, RootCategory> find = new Finder(Long.class, RootCategory.class);

	public static List<RootCategory> all(){
		return find.all();
	}

	public static RootCategory findById(Long id){
		return find.ref(id);
	}
}
