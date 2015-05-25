package models;

import java.util.List;

import javax.persistence.Entity;
import javax.persistence.Id;

import play.data.validation.Constraints.Required;
import play.db.ebean.Model;

@Entity
public class Item extends Model{
	@Id
	public Long id;
	@Required
	public String name;
	public Long design_id;
	public Long category_id;
	public String url;

	public static Finder<Long, Item> find = new Finder(Long.class, Item.class);

	public static List<Item> findAll(){
		return find.all();
	}

	public static Item findById(Long id){
		return find.ref(id);
	}

	public static List<Item> findByCategoryId(Long category_id){
		return find.where(
				"category_id = :category_id")
				.setParameter("category_id", category_id).findList();
	}


}
