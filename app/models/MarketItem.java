package models;

import java.util.List;

import javax.persistence.Entity;
import javax.persistence.Id;

import play.db.ebean.Model;

@Entity
public class MarketItem extends Model{
	@Id
	public Long id;
	public Long stars;
	public Long price;
	public String date;
	public Long exhibits;
	public Long item_id;

	public static Finder<Long, MarketItem> find = new Finder(Long.class, MarketItem.class);

	public static List<MarketItem> findAll(){
		return find.all();
	}



	public static List<MarketItem> findByCategoryId(Long item_id){
		return find.where(
				"item_id = :item_id")
				.setParameter("item_id", item_id).findList();
	}

}
