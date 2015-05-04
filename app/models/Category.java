package madels;

import play.data.validation.Constraints.*;
import play.db.ebean.*;
import javax.persistence.*;
import java.util.*;

@Entity
public class Category extends Model{
	@Id
	public Long id;
	@Required
	public String category_name;

	public static Finder<Long, Category> find = new Finder(Long.class, Category.class);

	public static List<Category> all(){
		return find.all();

	}

	public static Category findById(Long id){
		return find.ref(id);
	}
}




